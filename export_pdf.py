#!/usr/bin/env python3
"""
Capture every visible slide from slides.json and export a single PDF.

Unlike a vector export (which comes out <1 MB and can look soft when zoomed),
this renders each slide with Playwright at high resolution, waits for the
entrance animations to finish, screenshots the 1280x720 stage, and assembles
the images into one PDF.

It auto-tunes to land the file in a readable-but-shareable window
(default 2.5-9.5 MB): PNG (lossless) first; if that's too big it re-encodes to
JPEG and walks quality down; if it's too small it bumps the capture scale.

Usage:
    python3 export_pdf.py                       # -> MetaFloor_Deck.pdf
    python3 export_pdf.py out.pdf
    python3 export_pdf.py --scale 2 --min-mb 2 --max-mb 10
    python3 export_pdf.py --keep-frames         # leave the per-slide PNGs on disk
"""

import argparse
import asyncio
import json
import subprocess
import tempfile
from pathlib import Path

MB = 1024 * 1024
STAGE_SEL = ".stage"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export visible deck slides to a raster PDF.")
    p.add_argument("output_file", nargs="?", default="MetaFloor_Deck.pdf",
                   help="Output PDF filename (default: MetaFloor_Deck.pdf)")
    p.add_argument("--scale", type=int, default=3,
                   help="Capture device scale factor (3 = 3840x2160 per slide). Default 3.")
    p.add_argument("--min-mb", type=float, default=3.0, help="Lower size target in MB (default 3.0).")
    p.add_argument("--max-mb", type=float, default=9.5, help="Upper size target in MB (default 9.5).")
    p.add_argument("--settle-ms", type=int, default=1600,
                   help="Wait after load for entrance animations to finish (default 1600).")
    p.add_argument("--keep-frames", action="store_true", help="Keep the captured PNGs next to the PDF.")
    return p.parse_args()


async def capture_frames(slides, base: Path, out_dir: Path, scale: int, settle_ms: int):
    """Render each slide to a PNG of the stage. Returns list of PNG paths."""
    from playwright.async_api import async_playwright

    frames = []
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        # Exact stage size so deck.js renders at scale 1; device_scale_factor bumps DPI.
        page = await browser.new_page(
            viewport={"width": 1280, "height": 720}, device_scale_factor=scale
        )
        for i, slide in enumerate(slides):
            slide_path = base / slide["path"]
            print(f"  [{i + 1}/{len(slides)}] {slide.get('title', slide['path']):24s} <- {slide['path']}")
            await page.goto(slide_path.as_uri(), wait_until="networkidle")
            await page.wait_for_timeout(settle_ms)
            # Force fade-in helpers to their final state; hide the theme switcher chrome.
            await page.add_style_tag(
                content=".rise,.ci,.nr,.r{opacity:1!important;} .themer{display:none!important;}"
            )
            await page.wait_for_timeout(120)
            out = out_dir / f"slide_{i:02d}.png"
            stage = page.locator(STAGE_SEL).first
            if await stage.count():
                await stage.screenshot(path=str(out))
            else:  # slides without a .stage wrapper: full page
                await page.screenshot(path=str(out))
            frames.append(out)
        await browser.close()
    return frames


def flatten_png(path: Path) -> Path:
    """img2pdf rejects alpha PNGs; strip alpha in place if present."""
    from PIL import Image

    im = Image.open(path)
    if im.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", im.size, "white")
        im = im.convert("RGBA")
        bg.paste(im, mask=im.split()[-1])
        bg.save(path)
    return path


def png_to_jpeg(png: Path, jpg: Path, quality: int) -> Path:
    from PIL import Image

    Image.open(png).convert("RGB").save(jpg, "JPEG", quality=quality, optimize=True)
    return jpg


def assemble(image_paths, out_path: Path) -> int:
    subprocess.run(["img2pdf", *[str(p) for p in image_paths], "-o", str(out_path)],
                   check=True, capture_output=True)
    return out_path.stat().st_size


def main() -> None:
    args = parse_args()
    base = Path(__file__).resolve().parent
    with open(base / "slides.json", encoding="utf-8") as fh:
        slides = [s for s in json.load(fh)["slides"] if s.get("visible", True)]

    out_path = base / args.output_file
    min_b, max_b = args.min_mb * MB, args.max_mb * MB
    frame_dir = base / "_deck_frames" if args.keep_frames else Path(tempfile.mkdtemp(prefix="deck_"))
    frame_dir.mkdir(exist_ok=True)

    print(f"Capturing {len(slides)} slides at {args.scale}x -> {args.output_file}")
    frames = asyncio.run(capture_frames(slides, base, frame_dir, args.scale, args.settle_ms))
    for f in frames:
        flatten_png(f)

    # 1) Lossless PNG pass.
    size = assemble(frames, out_path)
    note = f"png @ {args.scale}x"

    # 2) Too small -> re-capture at a higher scale (once).
    if size < min_b and args.scale < 3:
        print(f"  {size/MB:.1f} MB is under target; re-capturing at 3x for crisper, larger output")
        frames = asyncio.run(capture_frames(slides, base, frame_dir, 3, args.settle_ms))
        for f in frames:
            flatten_png(f)
        size = assemble(frames, out_path)
        note = "png @ 3x"

    # 3) Too big -> walk JPEG quality down until it fits under max.
    if size > max_b:
        for q in (94, 90, 86, 82, 78, 74, 70, 66):
            jpgs = [png_to_jpeg(f, f.with_suffix(".jpg"), q) for f in frames]
            size = assemble(jpgs, out_path)
            note = f"jpeg q{q}"
            print(f"  jpeg q{q}: {size/MB:.1f} MB")
            if size <= max_b:
                break

    print(f"\nExported -> {out_path}")
    print(f"   {len(slides)} slides | {size/MB:.2f} MB | {note}")
    if size < min_b:
        print(f"   note: under {args.min_mb} MB target (deck is light on imagery) — raise --scale to grow it.")
    if size > max_b:
        print(f"   warning: still over {args.max_mb} MB — lower --scale.")
    if not args.keep_frames:
        import shutil
        shutil.rmtree(frame_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
