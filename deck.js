/* MetaFloor deck v3 — shared slide runtime.
   1. Uniform stage scaling (1280×720 design canvas → any viewport).
   2. Theme init + floating switcher (green | ember | violet), persisted in
      localStorage so the viewer and every standalone slide stay in sync. */
(function () {
  'use strict';

  var THEMES = ['sage', 'ember', 'violet'];
  var KEY = 'mf-theme';

  /* ---- scaling ---- */
  function fit() {
    /* 0.965 leaves a sliver of backdrop so the window shadow reads */
    var s = Math.min(window.innerWidth / 1280, window.innerHeight / 720) * 0.965;
    document.documentElement.style.setProperty('--stage-scale', String(s));
  }
  fit();
  window.addEventListener('resize', fit, { passive: true });

  /* ---- theme ---- */
  function currentTheme() {
    var q = new URLSearchParams(window.location.search).get('theme');
    if (THEMES.indexOf(q) !== -1) return q;
    try {
      var st = localStorage.getItem(KEY);
      if (THEMES.indexOf(st) !== -1) return st;
    } catch (_) {}
    return 'sage';
  }

  function applyTheme(t) {
    document.documentElement.setAttribute('data-theme', t);
    try { localStorage.setItem(KEY, t); } catch (_) {}
    var btns = document.querySelectorAll('.themer button');
    for (var i = 0; i < btns.length; i++) {
      btns[i].classList.toggle('on', btns[i].getAttribute('data-t') === t);
    }
  }

  function buildThemer() {
    var el = document.createElement('div');
    el.className = 'themer';
    THEMES.forEach(function (t) {
      var b = document.createElement('button');
      b.setAttribute('data-t', t);
      b.innerHTML = '<span class="sw"></span>' + t;
      b.addEventListener('click', function () { applyTheme(t); });
      el.appendChild(b);
    });
    document.body.appendChild(el);
  }

  function boot() {
    buildThemer();
    applyTheme(currentTheme());
    /* keep in sync when the viewer (same origin) switches theme */
    window.addEventListener('storage', function (e) {
      if (e.key === KEY && THEMES.indexOf(e.newValue) !== -1) applyTheme(e.newValue);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
