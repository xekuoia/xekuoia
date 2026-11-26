# Cómo se desarrolla xekuoia

La app publicada en `app/index.html` es un solo archivo HTML. No se edita a mano: se arma a partir de las piezas de esta carpeta.

## Piezas

| Archivo | Qué tiene |
|---|---|
| `v3.html` | Cabecera y CSS base (solo se usa hasta `</style>`) |
| `extra.css`, `extra2.css` | CSS agregado después (paneles, escenas, MIDI, grabación, marca) |
| `body.html` | Marcado de la interfaz |
| `app.js` | Toda la lógica: render WebGL2, capas, efectos, 3D, dibujo, sonido, MIDI, escenas, proyectos, exportar, grabar video, ayuda, traducciones |
| `assemble.py` | Une todo y escribe `app/index.html` |

## Armar la app

Desde la raíz del repo:

```
python3 src/assemble.py
```

Después de armarla, abrí `app/index.html` en Chrome o Edge (por ejemplo con `python3 -m http.server` desde la raíz y entrando a `http://localhost:8000/app/`).

## Publicar

- **xekuoia.com/app**: se publica sola con GitHub Pages al hacer push a `main`.
- **Versión en Claude** (artefacto "xekuoia"): republicar `app/index.html`.

## Reglas que conviene respetar

- Todo pasa en el navegador de quien la usa. No hay servidor ni cuentas, y no se guarda nada entre sesiones salvo preferencias en `localStorage` (claves `xekuoia-*` y `bastidor-*`).
- Los archivos de proyecto que abre la app son datos no confiables: todo valor se valida antes de usarse (ver `cleanVal`, `cleanAuto`, `loadScenes`).
- La única librería externa es Mediabunny (exportar MP4), cargada con SRI.
- Textos de la interfaz en español; el inglés sale del diccionario `DICT` y los patrones `PATS` de `app.js`.
- Colores y tipografías según el brand kit (ver `../brand/` y el contexto del proyecto).

## Licencia

GPL-3.0. Copyright © 2026 Sergio "Gio" Casabona.
