# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 579 (printed ٥٧٨)."""

PAGE_NUMBER = 579
PRINTED_PAGE = "٥٧٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لا أنها لا فائدة لها أصلا،» at the foot of PDF p. 578.
    {"type": "matn",
     "ar": "فإن لها فوائد في كلام العرب: إما معنوية وإما لفظية.",
     "en": "…for they have benefits in the speech of the Arabs, either semantic (maʿnawiyya) or verbal (lafẓiyya)."},
    {"type": "matn",
     "ar": "فالمعنوية: تأكيد المعنى كما في «من» الاستغراقية، و«الباء» في خبر «ما وليس».",
     "en": "The semantic [benefit] is the reinforcement of the meaning, as with the all-inclusive (istighrāqiyya) “min” and with “bāʾ” in the predicate of “mā” and “laysa”."},
    {"type": "matn",
     "ar": "وأما الفائدة اللفظية: فهي تزيين اللفظ، وكونه بزيادتها أفصح، أو كون الكلمة أو الكلام بسببها مهيئا لاستقامة وزن الشعر، أو لحسن السجع، أو غير ذلك.",
     "en": "As for the verbal benefit, it is the embellishment of the wording, its being more eloquent through their addition, or the word or the speech being made ready by them for the soundness of the poetic metre, or for the beauty of the rhymed prose (sajʿ), or other than that."},
    {"type": "matn",
     "ar": "ولا يجوز خلوها من الفائدتين معا، وإلا لعدت عبثا، ولا يجوز ذلك في كلام الفصحاء، ولا سيما في كلام الباري سبحانه وتعالى.",
     "en": "They cannot be devoid of both benefits together, otherwise they would be counted as vain (ʿabath); and that is not permissible in the speech of the eloquent, least of all in the speech of the Creator, Glorified and Exalted is He."},
    {"type": "matn",
     "ar": "(«إن»، و«أن») مخففتين (و«ما»، و«لا»، و«من»، و«الباء»، و«اللام»).",
     "en": "(“In” and “an”), both unstressed (mukhaffafatayn), (and “mā”, “lā”, “min”, “bāʾ” and “lām”)."},
    {"type": "matn",
     "ar": "(فـ«إن») بكسر الهمزة وسكون النون (تزاد مع «ما» النافية) كثيرا لتأكيد النفي، نحو: «ما إن رأيت زيدا» أي: ما رأيت زيدا.",
     "en": "(Thus “in”), with kasra on the hamza and a quiescent nūn, (is added with the negating “mā”), frequently, to reinforce the negation, as in “mā in raʾaytu Zaydan”, that is: I did not see Zayd."},
    {"type": "matn",
     "ar": "(وقلت) أي: زيادة «إن» (مع) «ما» (المصدرية)[[١]] نحو: «انتظرني ما إن جلس القاضي»، أي: مدة جلوسه،",
     "en": "(And it is rare), that is, the addition of “in”, (with) the (maṣdar-forming) “mā”, as in “intaẓirnī mā in jalasa al-qāḍī” (wait for me as long as the judge sits), that is, for the duration of his sitting;"},
    {"type": "matn",
     "ar": "(و) قلت: زيادتها أيضا مع (لما) نحو: «لما إن قام زيد قمت».",
     "en": "(and) its addition is also rare with (lammā), as in “lammā in qāma Zaydun qumtu” (when Zayd stood, I stood)."},
    {"type": "matn",
     "ar": "(و«أن») بفتح الهمزة وسكون النون (تزاد مع «لما») كثيرا نحو: ﴿فلما أن جاء البشير﴾[[٢]].",
     "en": "(And “an”), with fatḥa on the hamza and a quiescent nūn, (is added with “lammā”), frequently, as in “Then when (lammā an) the bearer of good news came”."},
    {"type": "matn",
     "ar": "(و) تزاد (بين «لو» والقسم) المتقدم عليه، نحو: «والله أن لو قام زيد قمت».",
     "en": "(And) it is added (between “law” and the oath) that precedes it, as in “wa-llāhi an law qāma Zaydun qumtu” (by Allah, had Zayd stood, I would have stood)."},
    {"type": "matn",
     "ar": "(وقلت) زيادتها (مع «الكاف») نحو:",
     "en": "(And) its addition (with “kāf”) (is rare), as in:"},
    {"type": "verse",
     "ar": "كأن ظبية تعطو إلى وارق السلم[[٣]]",
     "en": "as though a gazelle stretching up towards a leafy salam tree"},
    {"type": "matn",
     "ar": "على تقدير رواية ظبية بالجر.",
     "en": "on the assumption of the reading of “ẓabyatin” in the genitive."},
    {"type": "matn",
     "ar": "(و«ما») تزاد (مع «إذا») نحو: «إذا ما تخرج أخرج» بمعنى: إذا تخرج أخرج.",
     "en": "(And “mā”) is added (with “idhā”), as in “idhā mā takhruj akhruj”, meaning: when you go out, I go out;"},
    {"type": "matn",
     "ar": "(و) مع («متى») نحو: «متى ما تذهب أذهب».",
     "en": "(and) with (“matā”), as in “matā mā tadhhab adhhab” (whenever you go, I go)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وكذا الاسمية نحو قوله تعالى: ﴿ولقد مكناهم فيما إن مكناكم فيه﴾ (سورة الأحقاف: ٢٦)",
     "en": "Likewise the nominal [mā], as in His words, the Exalted: “And We had established them in that in which We have not established you” (Qurʾān, Sūrat al-Aḥqāf 46:26);"},
    {"type": "pair",
     "ar": "وبعد ألا للتنبيه نحو: ألا إن قام زيد.",
     "en": "and after the alerting “alā”, as in “alā in qāma Zaydun”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة يوسف: ٩٦.",
     "en": "Qurʾān, Sūrat Yūsuf 12:96."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ويروى إلى وارق السلم.",
     "en": "It is also transmitted as “ilā wāriq al-salam”."},
    # REVIEW: "وارق السلم" here is printed identically to the verse line; the variant
    # (commonly «ناضر السلم», cf. the gloss «والناضر» below) appears not to be printed.
    # REVIEW: «مثلثة وكعد» printed as such; the dictionary formula is likely «كعدو»; transcribed as printed.
    {"type": "pair",
     "ar": "العطو: التناول ورفع الرأس واليدين وظبي عطو مثلثة وكعد: يتطاول إلى الشجر ليتناول منه.",
     "en": "Al-ʿaṭw is reaching for something and raising the head and the forelegs; and a gazelle that is ʿaṭw (with any of the three vowels) and like “ʿad” [as printed] is one that stretches up to the tree to take from it."},
    {"type": "pair",
     "ar": "والناضر: الشديد الخضرة. والوارقة: الشجرة الخضراء، كل ذلك من القاموس.",
     "en": "Al-nāḍir is what is intensely green; and al-wāriqa is the green tree. All of that is from al-Qāmūs."},
]
