# Film camera UI explorations

Round 3: direction E only, in a black version and a silver version.

- Bottom controls follow the original sketch: shutter on the left, flash (Off / On / Auto) and a customizable button in the middle, camera roll on the right. Hold the custom button to choose Flip camera, Self-timer, Grid or Double exposure.
- In the silver version, the highlights on the brushed body, the chrome shutter, the black buttons and the phone frame follow device tilt. The page uses `deviceorientation` when the browser allows it and falls back to the pointer otherwise. The claude.ai artifact viewer blocks motion sensors.

Files:
- `index.html` is a standalone page. Open it on a phone over https to try the real gyro.
- `concepts.html` is the same content without the document wrapper. This is the source published as the artifact.

Earlier rounds (A–E, then the framed A, B and E) are in the git history.
