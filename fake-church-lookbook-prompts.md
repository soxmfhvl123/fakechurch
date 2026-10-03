# FAKE CHURCH — 모델 룩북 프롬프트

*모델 4명 고정 캐스팅 × 룩 20 + 그룹컷 4 + 주얼리 디테일 4 · 의상은 어패럴 라인(무지 블랙), 주얼리는 50종 라인업에서 매칭 · **배경은 전부 단색 블랙** — 장소 대신 조명(탑라이트·사이드·폰 글로우·래티스 그림자·레드 림)으로 컷마다 변주*

## 공통 스타일 블록 (모든 룩 프롬프트에 이미 포함됨)
```
fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

## 레퍼런스 지시문 (모든 룩·그룹 프롬프트 맨 앞에 이미 포함됨)
옷 사진만 넣을 때 — 기본
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. 
```
모델 얼굴 레퍼런스도 같이 넣을 때 — 얼굴을 **1번**, 옷을 2번부터 넣고 위 문장을 이걸로 교체
```
Image 1 is the face and body reference for the model; keep the face, hair and body identical. Images 2 onward are the exact clothing references; reproduce every garment exactly as shown, including every printed graphic, logo and blackletter lettering in the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. 
```

## 네거티브 (그래픽 보존용)
```
altered logo, redesigned graphic, misspelled or garbled lettering, missing print, extra text, extra logos, wrong garment color, changed garment fit, colorful clothing, gold jewelry, smiling, cheerful, plastic skin, overly retouched, extra fingers, deformed hands, cluttered, watermark
```


---

## STEP 1 — 모델 캐스팅 (캐릭터 고정)

룩북 20컷 내내 같은 얼굴이 나와야 하니까 **각 모델의 캐릭터 시트를 먼저 뽑아서 레퍼런스로 고정**한다 (Higgsfield Soul ID / 캐릭터 레퍼런스, 나노바나나는 이미지 레퍼런스로).

### M1 · DEACON (디콘)
**인물 묘사** — 아래 룩 프롬프트에 들어가는 고정 문구
```
a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear
```
**캐릭터 시트**
```
Character reference sheet of a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear, three views side by side: front view, side profile, back view, plus one close-up portrait, wearing a plain black t-shirt and black trousers, neutral standing pose, arms at sides, soft studio lighting, seamless pure black background, consistent face and proportions across all views, photorealistic, no jewelry, no text
```

### M2 · SISTER (시스터)
**인물 묘사** — 아래 룩 프롬프트에 들어가는 고정 문구
```
a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression
```
**캐릭터 시트**
```
Character reference sheet of a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression, three views side by side: front view, side profile, back view, plus one close-up portrait, wearing a plain black t-shirt and black trousers, neutral standing pose, arms at sides, soft studio lighting, seamless pure black background, consistent face and proportions across all views, photorealistic, no jewelry, no text
```

### M3 · ORACLE (오라클)
**인물 묘사** — 아래 룩 프롬프트에 들어가는 고정 문구
```
a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze
```
**캐릭터 시트**
```
Character reference sheet of a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze, three views side by side: front view, side profile, back view, plus one close-up portrait, wearing a plain black t-shirt and black trousers, neutral standing pose, arms at sides, soft studio lighting, seamless pure black background, consistent face and proportions across all views, photorealistic, no jewelry, no text
```

### M4 · CHOIR (콰이어)
**인물 묘사** — 아래 룩 프롬프트에 들어가는 고정 문구
```
an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression
```
**캐릭터 시트**
```
Character reference sheet of an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression, three views side by side: front view, side profile, back view, plus one close-up portrait, wearing a plain black t-shirt and black trousers, neutral standing pose, arms at sides, soft studio lighting, seamless pure black background, consistent face and proportions across all views, photorealistic, no jewelry, no text
```


---

## STEP 2 — 룩 (20컷)

| LOOK | 모델 | 조명 | 레퍼런스로 넣을 옷 (기획 기준 — 실제 가진 옷으로 바꿔도 됨) | 그래픽 정면 |
|---|---|---|---|---|
| 01 | M1 DEACON | TOP | an ankle-length black hooded cassock coat with a row of small covered buttons, worn over a black mock neck top, black straight-leg jeans | – |
| 02 | M2 SISTER | PHONE | an oversized black mesh football jersey, black straight-leg leather pants | – |
| 03 | M3 ORACLE | SIDE | a black leather biker jacket open over a black raw-cut sleeveless tank, black flared jeans | – |
| 04 | M4 CHOIR | KEY | a heavyweight oversized black pullover hoodie with the hood up, wide straight black sweatpants | ◎ 정면 |
| 05 | M1 DEACON | GOBO | a boxy heavyweight black short sleeve t-shirt, black cargo pants, a black leather belt with a silver buckle, a long silver wallet chain hanging from the belt | – |
| 06 | M2 SISTER | TOP | a cropped boxy black hoodie, long baggy black mesh basketball shorts, black crew socks | – |
| 07 | M3 ORACLE | BLUE | an all-black varsity jacket with black leather sleeves, a black mock neck top, black carpenter pants | – |
| 08 | M4 CHOIR | TOP | an ankle-length black hooded cassock coat with the hood up, a black knit balaclava | – |
| 09 | M1 DEACON | SIDE | a black MA-1 bomber jacket, black heavyweight sweat shorts, a black six-panel cap | – |
| 10 | M2 SISTER | RIM | an oversized black work shirt buttoned all the way up, black leather pants, black leather gloves | – |
| 11 | M3 ORACLE | BEAM | a boxy cropped black puffer jacket, black cargo pants | – |
| 12 | M4 CHOIR | KEY | an oversized black long sleeve t-shirt, black nylon snap-button track pants, a black trucker cap | ◎ 정면 |
| 13 | M1 DEACON | PHONE | a black leather biker jacket over a black boxy t-shirt, black flared jeans | – |
| 14 | M2 SISTER | RIM | a long black cassock coat worn open over a black waffle-knit thermal top | – |
| 15 | M3 ORACLE | RED | a black nylon coach jacket, black cuffed sweatpants, a black ribbed beanie | – |
| 16 | M4 CHOIR | SIDE | a black denim trucker jacket over a raw-edge black t-shirt, black straight-leg jeans | – |
| 17 | M1 DEACON | KEY | a heavyweight black crewneck sweatshirt, wide straight black sweatpants | ◎ 정면 |
| 18 | M2 SISTER | TOP | an oversized black sleeveless tank with raw-cut armholes, black cargo pants, a small black leather crossbody pouch | – |
| 19 | M3 ORACLE | BLUE | a black full-zip hoodie zipped up, black leather pants, a black bandana tied over the head | – |
| 20 | M4 CHOIR | KEY | a cropped boxy black t-shirt, wide black carpenter pants, a black leather belt with a silver buckle, a long silver wallet chain | – |

> 룩 프롬프트에는 옷 묘사를 넣지 않고 **「레퍼런스 옷 그대로」** 로만 지시함 — 텍스트로 옷을 묘사하면 레퍼런스와 충돌해서 그래픽이 바뀌거나 다른 옷이 섞임. 어떤 룩에 어떤 옷 사진을 넣을지는 이 표를 보고 고르면 됨.
> ◎ = 가슴/정면이 카메라를 향하는 컷 → 옷 그래픽이 가장 잘 보임.

### LOOK 01 · M1 DEACON · TOP light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear, wearing exactly the garments from the reference images, accessorized with a gothic cross pendant with mouse-pointer arrow tips hanging on a heavy chain of segmented halo links, a thick segmented halo band ring, standing perfectly centered facing the camera, hands at sides, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single overhead spotlight falling straight down like a halo, rest of the frame pure black, full body shot, low angle, symmetrical, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 02 · M2 SISTER · PHONE light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression, wearing exactly the garments from the reference images, accessorized with a long silver rosary necklace with small halo rings, round domed speaker-grille stud earrings, a twisted cable crown-of-thorns bangle, sitting sideways on a plain black stool, face lit by a phone held in hand, looking past the camera, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, lit only from below by a cold blue smartphone glow, three-quarter shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 03 · M3 ORACLE · SIDE light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze, wearing exactly the garments from the reference images, accessorized with a gothic plate-link choker with a central halo, thick segmented hoop earrings, a wide carved gothic cuff, walking toward the camera mid-stride, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single hard side light from the left, the other half of the body falling into black, full body shot, slightly low angle, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 04 · M4 CHOIR · KEY light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression, wearing exactly the garments from the reference images, accessorized with a rectangular silver dog tag on a ball chain, small mouse-pointer stud earrings, an oval stamp signet ring, standing straight facing the camera, arms relaxed at sides, chest fully visible, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single hard key light from upper left and a thin cool rim light separating the silhouette from the black, full body shot, eye level, centered, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 05 · M1 DEACON · GOBO light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear, wearing exactly the garments from the reference images, accessorized with a domed rose-window ring and a twisted cable thorn ring stacked on the hand, standing with one shoulder turned, hand raised near the face, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, hard light through a lattice pattern casting thin stripes of light and shadow across the body, half body shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 06 · M2 SISTER · TOP light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression, wearing exactly the garments from the reference images, accessorized with a hammered silver coin medallion pendant, a single small cross drop earring under a tiny halo, sitting on the floor with knees up, looking up at the camera, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single overhead spotlight falling straight down like a halo, rest of the frame pure black, full body shot, high angle, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 07 · M3 ORACLE · BLUE light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze, wearing exactly the garments from the reference images, accessorized with a square all-seeing-eye signet ring, an ornate church key pendant with a USB-shaped bit, standing with chin raised, one hand on hip, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single cold blue side light, three-quarter shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 08 · M4 CHOIR · TOP light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression, wearing exactly the garments from the reference images, accessorized with an open segmented halo pendant on a chain of round and cube-shaped silver beads, hands cupped together in front of the chest as if holding water, face mostly in shadow, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single overhead spotlight falling straight down like a halo, rest of the frame pure black, half body shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 09 · M1 DEACON · SIDE light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear, wearing exactly the garments from the reference images, accessorized with a heavy box chain carved with gothic quatrefoils, a hinged shackle-style bangle with a small padlock, crouching low, forearms resting on knees, staring into the camera, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single hard side light from the left, the other half of the body falling into black, full body shot, low angle, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 10 · M2 SISTER · RIM light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression, wearing exactly the garments from the reference images, accessorized with an oval saint medallion pendant, a tiny chalice drop earring, a two-finger gothic arch ring worn over the glove, standing still, hands folded at the waist, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, strong rim light outlining the silhouette from behind, almost no front light, full body shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 11 · M3 ORACLE · BEAM light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze, wearing exactly the garments from the reference images, accessorized with a twisted rope chain with small thorns, thorn cable hoop earrings, a silver spinner ring, half turned away, looking up toward the light, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single narrow beam of hard light from high above, full body shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 12 · M4 CHOIR · KEY light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression, wearing exactly the garments from the reference images, accessorized with a heavy curb chain with an oversized mouse-pointer clasp, a link bracelet of interlocking pointer-arrow links, walking toward the camera, arms relaxed, chest fully visible, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single hard key light from upper left and a thin cool rim light separating the silhouette from the black, full body shot, eye level, centered, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 13 · M1 DEACON · PHONE light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear, wearing exactly the garments from the reference images, accessorized with a sacred heart pendant with a one-bar battery icon carved across it, beaded huggie hoop earrings, kneeling with a glowing phone held between praying hands, eyes closed, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, lit only from below by a cold blue smartphone glow, three-quarter shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 14 · M2 SISTER · RIM light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression, wearing exactly the garments from the reference images, accessorized with a gothic reliquary locket with a tiny microchip behind glass, all-seeing-eye stud earrings, a silver rosary bracelet, standing with back to the camera, head turned over the shoulder toward the camera, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, strong rim light outlining the silhouette from behind, almost no front light, full body shot, back three-quarter view, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 15 · M3 ORACLE · RED light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze, wearing exactly the garments from the reference images, accessorized with a necklace chain of small hammered halo coins, a chunky chain bracelet with coin charms, standing with hands in jacket pockets, weight on one leg, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, a single dim red rim light from behind as the only color in the frame, front of the body in deep shadow, full body shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 16 · M4 CHOIR · SIDE light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression, wearing exactly the garments from the reference images, accessorized with a miniature rubber-stamp shaped pendant, rectangular stamp-border stud earrings, a progress-bar band ring, a slim beaded bangle, seated on a plain black stool in profile, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single hard side light from the left, the other half of the body falling into black, half body shot, profile, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 17 · M1 DEACON · KEY light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear, wearing exactly the garments from the reference images, accessorized with a heavy chain of segmented halo links, a single segmented halo hoop earring, sitting on a low plain black stool facing the camera, elbows on knees, chest fully visible, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single hard key light from upper left and a thin cool rim light separating the silhouette from the black, full body shot, eye level, centered, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 18 · M2 SISTER · TOP light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression, wearing exactly the garments from the reference images, accessorized with a round rose-window pendant layered with a pointer-arrow cross pendant, standing with arms crossed, staring at the camera, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single overhead spotlight falling straight down like a halo, rest of the frame pure black, three-quarter shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 19 · M3 ORACLE · BLUE light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze, wearing exactly the garments from the reference images, accessorized with a small chalice pendant etched with circuit traces, a sculpted chalice ring, holding one hand up toward an off-frame light, light falling on the palm and face, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single cold blue side light, half body shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### LOOK 20 · M4 CHOIR · KEY light
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression, wearing exactly the garments from the reference images, accessorized with a tiny ornate church key drop earring, stacked carved silver rings, sitting on a plain black box, one leg extended, looking straight at the camera, against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single hard key light from upper left and a thin cool rim light separating the silhouette from the black, full body shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```


---

## STEP 3 — 그룹컷 (4컷)

> 인물 4명을 한 번에 일관되게 뽑기는 어려움 → 그룹컷은 **4명 캐릭터 시트를 레퍼런스로 같이 넣거나**, 배경만 뽑고 인물을 1명씩 합성하는 게 안정적.

### G1 · 전원 · 일렬 정렬
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. all four models standing in a straight symmetrical line facing the camera like clergy, all wearing garments from the reference images — the four models are [DEACON: a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear; SISTER: a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression; ORACLE: a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze; CHOIR: an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression], against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single overhead spotlight falling straight down like a halo, rest of the frame pure black, wide full body group shot, perfectly symmetrical, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### G2 · 전원 · 벤치
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. all four models sitting side by side on one long plain black bench facing the camera, faces lit from below by their phones, all wearing garments from the reference images — the four models are [DEACON: a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear; SISTER: a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression; ORACLE: a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze; CHOIR: an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression], against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, lit only from below by a cold blue smartphone glow, wide group shot, eye level, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### G3 · 전원 · 레드 림
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. all four models standing in scattered poses, each outlined by a red rim light, all wearing garments from the reference images — the four models are [DEACON: a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear; SISTER: a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression; ORACLE: a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze; CHOIR: an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression], against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, a single dim red rim light from behind as the only color in the frame, front of the body in deep shadow, wide full body group shot, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```

### G4 · 전원 · 최후의 만찬
```
Use the attached clothing reference images as the exact outfit. Reproduce every garment exactly as shown in the references: same cut, silhouette, fit, fabric, black color, and every printed graphic, logo and blackletter lettering in exactly the same position, size, spelling and style. Do not redesign, remove, add, move or distort any logo or text on the clothing. Clothing graphics must stay sharp and readable and follow the fabric folds naturally. all four models seated along one side of a long plain black table in a composition reminiscent of a classical last supper painting, glowing smartphones on the table like bread and wine, all wearing garments from the reference images — the four models are [DEACON: a Korean man in his late 20s, tall and lean, very short buzz cut black hair, sharp cheekbones, pale skin, thin dark eyebrows, calm stoic expression, small silver hoop in left ear; SISTER: a Korean woman in her mid 20s, long sleek straight black hair center-parted, pale porcelain skin, sharp minimal black eyeliner, bare lips, cold serene expression; ORACLE: a Black woman in her late 20s, clean shaved head, high cheekbones, deep brown skin with natural glow, strong brows, intense steady gaze; CHOIR: an androgynous East Asian model in their mid 20s, short choppy bleached platinum blonde hair, very pale skin, delicate features, faint freckles, blank unreadable expression], against a seamless pure black backdrop, plain solid black background with no environment, no props, no set, single overhead spotlight falling straight down like a halo, rest of the frame pure black, wide group shot, frontal, symmetrical, fashion lookbook editorial photography, shot on 35mm film, fine film grain, low-key dramatic chiaroscuro lighting, overall very dark image, background falling off into near-black shadow with only the model lit, crushed deep blacks, desaturated palette of deep black, bone white and chrome silver, cinematic composition, realistic high detail skin texture, heavy oxidized sterling silver jewelry catching the light, 4:5 vertical, no watermark, no overlaid captions
```


---

## STEP 4 — 착용 디테일 (주얼리 상세페이지용 4컷)

### D01 · 손 · 반지 스택
```
Close-up of two hands clasped in prayer, fingers stacked with heavy carved oxidized sterling silver rings, black sleeve cuffs visible, pale skin, deep shadow background, single hard side light, shot on 35mm film, fine film grain, desaturated palette of deep black, bone white and chrome silver, shallow depth of field, realistic skin texture, any visible clothing matches the reference images exactly, 4:5 vertical
```

### D02 · 목 · 레이어드 체인
```
Close-up of a neck and collarbone wearing several layered heavy sterling silver chains and gothic pendants over a black t-shirt collar, cropped below the lips, chiaroscuro light, shot on 35mm film, fine film grain, desaturated palette of deep black, bone white and chrome silver, shallow depth of field, realistic skin texture, any visible clothing matches the reference images exactly, 4:5 vertical
```

### D03 · 귀 · 이어링
```
Close-up profile of an ear with stacked heavy silver hoop and stud earrings, short hair, black collar visible, dark background, rim light, shot on 35mm film, fine film grain, desaturated palette of deep black, bone white and chrome silver, shallow depth of field, realistic skin texture, any visible clothing matches the reference images exactly, 4:5 vertical
```

### D04 · 손목 · 폰을 쥔 손
```
Close-up of a hand holding a glowing smartphone, wrist stacked with a heavy silver chain bracelet and a carved gothic cuff, black sleeve, phone light on the silver, shot on 35mm film, fine film grain, desaturated palette of deep black, bone white and chrome silver, shallow depth of field, realistic skin texture, any visible clothing matches the reference images exactly, 4:5 vertical
```


---

## 워크플로우 (추천 순서)
1. **캐릭터 시트 4장** 생성 → 마음에 드는 얼굴로 확정, 레퍼런스 고정
2. **룩 생성** — 두 가지 방법
   - **A. 텍스트로**: 위 LOOK 프롬프트 + 캐릭터 레퍼런스 → 빠르지만 옷·주얼리 디테일이 상품 썸네일과 조금 달라질 수 있음
   - **B. 상품 썸네일로 입히기 (일관성 ↑, 추천)**: 이미 뽑은 어패럴/주얼리 썸네일을 레퍼런스로 넣고 나노바나나에
     ```
     Dress the model from image 1 in the garment from image 2 and the jewelry from image 3. Keep the model's face, hair and body exactly the same. Keep the garment's cut, fabric and fit exactly as shown. Pose: [POSE]. Setting: [LOCATION]. Lighting: dramatic chiaroscuro, 35mm film grain, desaturated black, bone white and chrome silver.
     ```
     → `[POSE]`, `[LOCATION]`은 위 LOOK 프롬프트에서 그대로 복사
3. **로고 합성** — ◎ 컷 위주로 어패럴 문서의 나노바나나 합성 프롬프트 사용 (같은 로고·같은 프린트 방식을 상품 썸네일과 맞출 것)
4. **후보정** — 그레인·톤 통일, 레드는 네온 십자가와 FAKE 도장에만 (사이트 컬러 규칙과 동일)

## 파일명
`LOOK01_M1_nave.jpg` / `G01_nave.jpg` / `D01_hands.jpg`
