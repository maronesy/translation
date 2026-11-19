# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 581 (printed ٥٨٠)."""

PAGE_NUMBER = 581
PRINTED_PAGE = "٥٨٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وشذت) زيادتها (مع المضاف) كقوله:» at the foot of PDF p. 580.
    # The verse is printed with only its first hemistich; the second is a row of dots.
    {"type": "verse",
     "ar": "في بئر لا حور سرى، وما شعر     ……………………",
     "en": "…in a well of no return (lā ḥūrin) he went by night, and he did not perceive …"},
    {"type": "matn",
     "ar": "أي: في بئر حور، والحور: المهلكة جمع حائر أي: هالك من حار أي: هلك.",
     "en": "That is: in a well of ḥūr; and al-ḥūr is the place of perdition, the plural of ḥāʾir, that is, one perishing, from ḥāra, that is, he perished."},
    {"type": "matn",
     "ar": "(و«من»، و«الباء»، و«اللام» تقدم ذكرها) مشتملا على ذكر مواضع زيادتها، فلا حاجة إلى تكرارها.",
     "en": "(And “min”, “bāʾ” and “lām” have been mentioned before), [that mention] including the places where they are added, so there is no need to repeat them."},

    {"type": "section", "ar": "[حرفا التفسير]",
     "en": "The Two Particles of Explication (ḥarfā al-tafsīr)"},

    {"type": "matn",
     "ar": "(حرفا التفسير: «أي»، وهي لتفسير كل مبهم[[١]] من المفرد) نحو: «جاءني زيد أي: أبو عبد الله»",
     "en": "(The two particles of explication: “ay”, which serves to explicate every vague expression, whether a single word), as in “jāʾanī Zaydun ay Abū ʿAbd Allāh” (Zayd came to me, that is, Abū ʿAbd Allāh),"},
    {"type": "matn",
     "ar": "(والجملة) كما تقول: «قطع رزقه أي: مات».",
     "en": "(or a sentence), as when you say “quṭiʿa rizquhu ay māta” (his sustenance was cut off, that is, he died)."},
    {"type": "matn",
     "ar": "(و«أن» وهي) أي: «أن» (مختصة بما في معنى القول[[٢]]) أي: بفعل متقرر في معنى القول تقرر المظروف في الظرف غير منفك عنه،",
     "en": "(And “an”; and it), that is, “an”, (is restricted to what is in the sense of saying), that is, to a verb that is lodged in the sense of saying as the contained is lodged in its container, inseparable from it;"},
    {"type": "matn",
     "ar": "فلا تقع بعد صريح القول، ولا بعد ما ليس في معنى القول.",
     "en": "so it does not occur after an explicit verb of saying, nor after what is not in the sense of saying."},
    {"type": "matn",
     "ar": "فهي لا تفسر في الأكثر إلا مفعولا مقدرا للفظ غير صريح القول مؤد معناه",
     "en": "Thus, for the most part, it explicates only an implied object of a word that is not explicitly “saying” but conveys its meaning,"},
    {"type": "matn",
     "ar": "نحو قوله تعالى: ﴿وناديناه أن يا إبراهيم﴾[[٣]]، فقوله: «أن يا إبراهيم» تفسير لمفعول «ناديناه» المقدر، أي: ناديناه بلفظ هو قولنا: يا إبراهيم،",
     "en": "as in His words, the Exalted: “And We called to him: (an) O Ibrāhīm”; His words “an yā Ibrāhīm” are an explication of the implied object of “nādaynāhu”, that is: We called to him with an utterance, namely Our saying “O Ibrāhīm”;"},
    {"type": "matn",
     "ar": "وكذلك قولك: «كتبت إليه أن ائت» أي: كتبت إليه شيئا هو «ائت».",
     "en": "and likewise your saying “katabtu ilayhi an iʾti” (I wrote to him: come), that is: I wrote to him something, namely “come”."},
    {"type": "matn",
     "ar": "فـ«أن» حرف دال على أن «ائت» تفسير للمفعول به المقدر لـ«كتبت»،",
     "en": "So “an” is a particle indicating that “iʾti” is an explication of the implied direct object of “katabtu”."},
    {"type": "matn",
     "ar": "وقوله تعالى: ﴿ما قلت لهم إلا ما أمرتني به أن اعبدوا الله﴾[[٤]]، فقوله: «أن اعبدوا الله» تفسير للضمير في «به»، وفي «أمرت» معنى القول،",
     "en": "And His words, the Exalted: “I said to them only what You commanded me: (an) worship Allah”; His words “an uʿbudū Allāh” are an explication of the pronoun in “bihi”, and “amarta” carries the sense of saying;"},
    {"type": "matn",
     "ar": "وليس تفسيرا لما في قوله: «ما أمرتني»؛ لأنه مفعول لصريح القول.",
     "en": "it is not an explication of the “mā” in his words “mā amartanī”, because that is the object of an explicit verb of saying."},
    {"type": "matn",
     "ar": "وقد يفسر بها المفعول به الظاهر كقوله تعالى: ﴿إذ أوحينا إلى أمك ما يوحى أن اقذفيه﴾[[٥]]، فقوله: «أن اقذفيه» تفسير لـ«ما يوحى» الذي هو",
     "en": "An explicit direct object is sometimes explicated by it, as in His words, the Exalted: “When We revealed to your mother what was revealed: (an) cast him”; His words “an iqdhifīhi” are an explication of “mā yūḥā”, which is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: «تفسير الغير» printed as such (one expects «تفسيرا لغير»); transcribed as printed.
    {"type": "pair",
     "ar": "قال ابن مالك: الغالب فيه أن يكون تفسير الغير ما في معنى القول.",
     "en": "Ibn Mālik said: what predominates in it is that it be an explication of what is other than [that which is] in the sense of saying."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى توجيه ظرفية المعنى للفظ بأن المعنى ظرف اعتباري يستعار له أداة الظرف،",
     "en": "This alludes to the justification of the meaning’s being a container for the word: the meaning is a notional (iʿtibārī) container, for which the particle of containment is borrowed."},
    {"type": "pair",
     "ar": "نعم اعتبار للفظ ظرفا للمعنى هو الشائع حتى قال الهندي: إنه على القلب،",
     "en": "Admittedly, regarding the word as a container for the meaning is what is common, so that al-Hindī said that it is by inversion (ʿalā al-qalb);"},
    {"type": "pair",
     "ar": "لكن جعل القلب قسما للظرفية للاعتبارات حيث قال: الظرفية اعتبارية أو على القلب.",
     "en": "but he made inversion a division opposite to notional containment, for he said: the containment is either notional or by inversion."},
    # REVIEW: «للظرفية للاعتبارات» printed as such (one expects «للظرفية الاعتبارية»); transcribed as printed.
    {"type": "pair",
     "ar": "وفيه أن ظرفية اللفظ للمعنى أيضا اعتبارية.",
     "en": "Against this: the word’s being a container for the meaning is also notional."},

    # ---------------- Footnotes 3-5 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair", "ar": "سورة الصافات: ١٠٤.", "en": "Qurʾān, Sūrat al-Ṣāffāt 37:104."},
    {"type": "note", "num": "٤"},
    {"type": "pair", "ar": "سورة المائدة: ١١٧.", "en": "Qurʾān, Sūrat al-Māʾida 5:117."},
    {"type": "note", "num": "٥"},
    {"type": "pair", "ar": "سورة طه: ٣٨-٣٩.", "en": "Qurʾān, Sūrat Ṭāhā 20:38–39."},
]
