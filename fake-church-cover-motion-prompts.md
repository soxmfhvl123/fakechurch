# FAKE CHURCH — 커버 모션 프롬프트 (THE LAST SUPPER)

*입력: 완성된 커버 이미지 (13인 · 블랙 배경 · 흑백 · 테이블 위 빛나는 폰) → 이미지 투 비디오*

## 공통 세팅
- **입력 이미지** = 시작 프레임 (start frame)
- **비율**: 원본이 약 2:1 → 16:9 출력이면 위아래 블랙 여백이 살짝 잘림 (인물 손실 없음). 21:9 지원 모델이면 21:9
- **길이**: 모델이 5초/10초 단위 → 아래는 **10초 2종 + 5초 1종**, 타임코드는 초 단위로 프롬프트에 그대로 포함
- **루프용(M01)**: 끝 프레임(end frame) 지정 가능한 모델이면 **시작=끝 프레임을 같은 이미지로** 넣기 → 웹사이트 히어로에서 끊김 없이 반복

## 공통 보존 문구 (모든 프롬프트에 이미 포함)
```
Keep exactly thirteen people, the same faces, hair, black clothing and every printed logo and blackletter lettering unchanged and readable, the same silver jewelry, the same table, glowing phones, chalices and chains. The background stays pure black at all times. No new people, no new objects, no camera cuts, no text overlays. High-contrast black and white 35mm film look with fine grain throughout.
```

## 네거티브
```
color, camera shake, scene cut, new people, people leaving the frame, morphing faces, warping hands, extra fingers, melting clothing, changing logos, garbled lettering, background lights, room, windows, fast motion, talking, smiling, eating
```

---

## M01 · 히어로 루프 — 살아있는 그림 (10초)
*웹사이트 커버 배경용. 카메라 고정, 아주 미세한 움직임만. 마지막 2초에 원래 포즈로 돌아와 루프.*

| 초 | 동작 |
|---|---|
| 0–2 | 완전한 정적. 필름 그레인과 폰 화면 빛이 숨쉬듯 아주 약하게 밝아졌다 어두워짐 |
| 2–4 | 좌우 그룹이 원작 제스처를 이어가듯 미세하게 움직임 — 고개가 몇 도 돌아가고, 펼친 손이 천천히 흔들림. 중앙 인물은 미동 없음 |
| 4–6 | 왼쪽에서 4번째, 폰을 쥔 인물이 화면을 내려다보고, 폰 빛이 얼굴을 더 밝힘. 실버 체인이 몸의 움직임에 따라 반짝 |
| 6–8 | 오른쪽 그룹의 손가락이 천천히 가리키는 동작, 기대어 있던 인물이 살짝 자세를 고침 |
| 8–10 | 모두 천천히 처음 포즈로 돌아와 시작 프레임과 같은 상태로 정지 |

```
Static locked-off camera, no camera movement. The image comes alive like a living painting with very subtle, slow, solemn motion. 0–2s: complete stillness, only the film grain flickers and the phone screens on the table gently pulse brighter and dimmer like breathing. 2–4s: the groups of figures on both sides continue their gestures from the painting with tiny slow movements — heads turn a few degrees, open hands drift slightly — while the central figure stays perfectly still with eyes lowered. 4–6s: the figure fourth from the left holding a phone slowly looks down at its screen and the screen light brightens on his face; silver chains glint as bodies shift. 6–8s: on the right side a raised hand slowly points, a leaning figure settles slightly. 8–10s: everyone slowly returns to their exact original pose and the frame comes to rest identical to the first frame, ready to loop. Keep exactly thirteen people, the same faces, hair, black clothing and every printed logo and blackletter lettering unchanged and readable, the same silver jewelry, the same table, glowing phones, chalices and chains. The background stays pure black at all times. No new people, no new objects, no camera cuts, no text overlays. High-contrast black and white 35mm film look with fine grain throughout.
```

---

## M02 · 시네마틱 푸시인 → 블랙아웃 (10초)
*인트로 / 런칭 티저용. 마지막 블랙 화면에 FAKE CHURCH 워드마크·도장 얹기 좋음.*

| 초 | 동작 |
|---|---|
| 0–3 | 와이드 고정. 정적, 폰 빛만 미세하게 깜빡 |
| 3–7 | 아주 느린 달리 푸시인 — 중앙 인물을 향해 전진, 좌우 끝 인물들이 프레임 밖으로 서서히 빠짐. 주변 인물들 미세하게 움직임 |
| 7–8.5 | 중앙 인물이 천천히 눈을 들어 렌즈를 정면으로 응시 |
| 8.5–9.5 | 테이블 위 모든 폰 화면이 동시에 한 번 강하게 번쩍 |
| 9.5–10 | 컷 없이 전체가 순흑으로 페이드아웃 |

```
0–3s: wide locked-off frame exactly as the image, stillness, only the phone screens on the table flicker faintly. 3–7s: a very slow, smooth dolly push-in straight toward the central figure along the one-point perspective, the outermost figures on both sides gradually leave the frame edges, the surrounding figures make tiny slow movements. 7–8.5s: the central figure with platinum hair slowly lifts their eyes from the table and stares directly into the lens, expressionless. 8.5–9.5s: every phone screen on the table flares bright white at the same instant, lighting all the hands and faces from below. 9.5–10s: the whole frame fades smoothly to pure black, no cut. Keep exactly thirteen people, the same faces, hair, black clothing and every printed logo and blackletter lettering unchanged and readable, the same silver jewelry, the same table, glowing phones, chalices and chains. The background stays pure black at all times. No new people, no new objects, no camera cuts, no text overlays. High-contrast black and white 35mm film look with fine grain throughout.
```

---

## M03 · 폰이 꺼지는 순간 (5초 · SNS 숏폼)
*짧고 섬뜩한 한 방. 릴스/스토리 첫 장면용.*

| 초 | 동작 |
|---|---|
| 0–1 | 원본 그대로 정적 |
| 1–1.5 | 테이블 위 모든 폰 화면이 동시에 꺼짐 → 얼굴의 아래 조명이 사라지고 화면이 더 어두워짐 |
| 1.5–3 | 거의 암흑, 실버 주얼리와 흰 레터링만 희미하게 빛남. 모두 정지 |
| 3–3.5 | 폰이 이전보다 밝게 동시에 다시 켜짐 |
| 3.5–5 | 13명 전원이 일제히 고개를 돌려 렌즈를 정면으로 응시하며 정지 |

```
Static locked-off camera. 0–1s: complete stillness exactly as the image. 1–1.5s: every phone screen on the table switches off at the same instant, the light from below disappears from all faces and hands and the frame drops into near darkness. 1.5–3s: almost total darkness, only faint glints of the silver jewelry and the white lettering on the clothing remain visible, nobody moves. 3–3.5s: all the phone screens snap back on at once, brighter than before, lighting every face from below. 3.5–5s: all thirteen people turn their heads in perfect unison and stare directly into the lens, then freeze, expressionless. Keep exactly thirteen people, the same faces, hair, black clothing and every printed logo and blackletter lettering unchanged and readable, the same silver jewelry, the same table, glowing phones, chalices and chains. The background stays pure black at all times. No new people, no new objects, no camera cuts, no text overlays. High-contrast black and white 35mm film look with fine grain throughout.
```

---

## 편집 가이드
- **웹사이트 커버**: M01 10초 루프 (`autoplay muted loop playsinline`) — 정지 이미지를 poster로 깔고 영상 로드되면 교체
- **런칭 티저 (총 15초)**: M03(5초) → M02(10초), M02 마지막 블랙에서 워드마크 + FAKE 도장이 "쾅" (사이트 히어로 애니메이션과 동일 타이밍: 0.15초)
- **사운드 붙일 경우**: M02 8.5초 폰 플래시 / M03 1초 소등·3초 재점등에 저음 임팩트

## 팁
- **13명 얼굴·손이 뭉개질 때**: 움직임이 클수록 무너짐 → `very subtle`, `tiny`, `slow`를 더 강하게. 그래도 무너지면 움직이는 인물을 2~3명으로 한정 (`only the figure fourth from the left moves`)
- **M03 일제히 고개 돌리기**가 어긋나면 → 3.5–5초 구간만 `the central five figures turn their heads`로 축소
- **레터링 깨짐**: 의상 그래픽은 움직임 적은 인물에 두는 게 안전 — 중앙 인물(가슴 로고)은 모든 버전에서 정지 or 시선만 이동하도록 설계됨
- **파일명**: `COVER_M01_loop_10s.mp4`, `COVER_M02_pushin_10s.mp4`, `COVER_M03_phones-off_5s.mp4`
