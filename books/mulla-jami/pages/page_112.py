# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 112 (printed ١١١)."""

PAGE_NUMBER = 112
PRINTED_PAGE = "١١١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "(وإذا صرف[[١]]) أي: سراويل لعدم تحقق جمعيته تحقيقا، والأصل في الأسماء الصرف (فلا إشكال) بالنقض به على قاعدة الجمع[[٢]]، ليحتاج إلى التفصي عنه.",
     "en": "“And when it is declined” — that is, sarāwīl, because its plurality is not realized in fact, while the default in nouns is declension — “then there is no difficulty” by [its] contradicting the rule of the plural, such that one would need to extricate oneself from it."},

    {"type": "matn",
     "ar": "(ونحو: جوار) أي: كل جمع منقوص[[٣]] على «فواعل» يائيا كان أو واويا كالجواري والدواعي[[٤]] (رفعا وجرا) أي: في حالتي الرفع والجر[[٥]] (كـ«قاض») أي: حكمه حكم «قاض»، بحسب الصورة في حذف الياء عنه، وإدخال التنوين عليه،",
     "en": "“And [words] like jawārin” — that is, every defective plural (jamʿ manqūṣ) of the pattern fawāʿil, whether its final radical is yāʾ or wāw, such as al-jawārī and al-dawāʿī — “in the nominative and genitive,” that is, in the two states of rafʿ and jarr, “[behave] like qāḍin”; that is, its ruling is the ruling of “qāḍin” with respect to outward form, in dropping the yāʾ from it and admitting nunation (tanwīn) upon it."},

    {"type": "matn",
     "ar": "تقول: «جاءتني جوار»، و«مررت بجوار»، كما تقول: «جاءني قاض»، و«مررت بقاض».",
     "en": "You say “jāʾatnī jawārin” and “marartu bi-jawārin,” just as you say “jāʾanī qāḍin” and “marartu bi-qāḍin.”"},

    {"type": "matn",
     "ar": "وأما في حالة النصب فالياء متحركة مفتوحة، نحو: «رأيت جواري»، فلا إشكال في حالة النصب؛ لأن الاسم غير منصرف للجمعية مع صيغة منتهى الجموع، بخلاف حالتي الرفع والجر، فإنه قد اختلف فيه؟",
     "en": "As for the accusative state, the yāʾ is vowelled with fatḥa, as in “raʾaytu jawāriya,” so there is no difficulty in the accusative state — because the noun is non-declinable on account of plurality together with [its being of] the pattern of the utmost plurals (ṣīghat muntahā al-jumūʿ) — unlike the two states of rafʿ and jarr, over which there has indeed been disagreement."},

    {"type": "matn",
     "ar": "فذهب بعضهم: إلى أن الاسم منصرف، والتنوين فيه تنوين الصرف؛ لأن الإعلال المتعلق بجوهر الكلمة[[٦]] مقدم على منع الصرف الذي هو من أحوال الكلمة بعد تمامها،",
     "en": "Some held that the noun is declinable, and that the nunation in it is the nunation of declension (tanwīn al-ṣarf) — because the morphophonemic alteration (iʿlāl) pertaining to the very substance of the word takes precedence over the withholding of declension, which is among the accidents of the word after its completion;"},

    {"type": "matn",
     "ar": "فأصل «جوار»[[٧]] في قولك: «جاءتني جوار»: «جواري» بالضم والتنوين، بناء",
     "en": "so the original of “jawārin” in your saying “jāʾatnī jawārin” is “jawārīu” with ḍamma and nunation, on the basis…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لما كان عدم الصرف غالبا، والصرف مغلوبا كان لفظ «إذا» في الأول واقعا موقعه، وفي الثاني واقعا موقع «إن» للمشاكلة.",
     "en": "Since non-declension is predominant and declension the lesser [case], the word “idhā” (“when”) in the first [instance] falls in its [proper] place, whereas in the second it falls in the place of “in” (“if”) for the sake of formal parallelism (mushākala)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يخفى أن نفي جنس الإشكال بهذا المعنى لا ينافي إثبات الإشكال من وجه آخر، هو أن سراويل إذا صرف كان ينبغي أن يصرف مصابيح؛ لأنه يوازن مفردا كما يصرف فرازنة؛ لأنه يوازن كراهية.",
     "en": "It is not hidden that negating the genus of the difficulty in this sense does not preclude establishing the difficulty from another angle — namely, that if sarāwīl is declined, then maṣābīḥ ought [likewise] to be declined, since it parallels a singular [in pattern], just as farāzina is declined because it parallels karāhiya."},
    {"type": "pair",
     "ar": "ويمكن أن يدفع بأن سراويل مفرد أعجمي، ولا اعتبار لموازنة الأعجمي أو بالندور أو بتقدير الجمع في سراويل مطلقا صرف أو لم يصرف. وذلك لاختصاص هذا الوزن بالجمع.",
     "en": "This may be repelled by [noting] that sarāwīl is a foreign singular, and no account is taken of the parallelism of a foreign [word]; or [it is settled] by rarity, or by the supposition of plurality in sarāwīl absolutely, whether it is declined or not — and that is because this pattern is proper to the plural."},
    {"type": "pair",
     "ar": "فمن نظر إلى التقدير منعه من الصرف. ومن نظر إلى وقوعه على الواحد صرفه.",
     "en": "So whoever looks to the supposition [of plurality] withholds it from declension, and whoever looks to its applying to the single [thing] declines it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وكذا كل مفرد غير منصرف منقوص كقاض اسم امرأة، وأعيل مصغر لا مقصور كأعلى، فإن الألف فيه ثابتة لخفتها.",
     "en": "And likewise every non-declinable defective (manqūṣ) singular, such as “Qāḍin” as a woman’s name, and “Uʿayl” as a diminutive — [this holds] not for a shortened noun (maqṣūr) like “aʿlā,” for the alif in it is fixed on account of its lightness."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "مثال للجمع المنقوص الواوي، فإنه جمع داعية، هي في الأصل داعوة من الدعوة.",
     "en": "[This is] an example of the wāwī defective plural, for it is the plural of dāʿiya, which is originally dāʿiwa from al-daʿwa."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني رفعا وجرا ظرف، فهو متعلق بمعنى النحو. ولما لم يقيد المشبه به بكونه في وقت الرفع والجر، وهو أيضا مقيد به، أصلحه الشارح بتأويل قوله: كقاض بأن المراد منه أن حكمه حكم قاض بحسب الصورة إلى آخره.",
     "en": "He means that “rafʿan wa-jarran” is an adverbial [accusative] (ẓarf), so it is connected to the sense of “naḥw” (the resemblance implied by “such as”). And since the object of comparison (al-mushabbah bihi) was not restricted to its being at the time of rafʿ and jarr — while it too is [so] restricted — the commentator rectified it by interpreting his statement “like qāḍin” [to mean] that what is intended by it is that its ruling is the ruling of qāḍin with respect to outward form, and so on."},
    {"type": "pair",
     "ar": "والأظهر أن مراده به أن مراد المصنف رحمه الله أنه مثله بحسب الصورة لا من كل وجه، حتى يكون حاكما بانصرافه.",
     "en": "But the more evident [reading] is that what he intends by it is that the author’s intent, may Allah have mercy on him, is that it resembles it (qāḍin) with respect to outward form, not in every respect — [for otherwise] he would be judging it to be declinable."},
    {"type": "pair",
     "ar": "قال عبد الغفور: إشارة إلى أنهما منصوبتان على الظرفية، والعامل فيهما المماثلة المستفادة من الكاف.",
     "en": "ʿAbd al-Ghafūr said: [it is] an indication that the two [words, rafʿan and jarran] are in the accusative as adverbials (ẓarfiyya), the governing operator in them being the likeness derived from the kāf [of comparison]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ولأن الإعلال سببه قوي، وهو الاستثقال المحسوس، ومنع الصرف سببه ضعيف، وهو مشابهة غير محسوسة.",
     "en": "And because the cause of iʿlāl is strong — namely, the perceptible heaviness of pronunciation (al-istithqāl al-maḥsūs) — whereas the cause of withholding declension is weak, namely an imperceptible resemblance."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "إلى قوله: بناء على أن الأصل في الاسم الصرف فيه أن الصرف أيضا من أحوال الكلمة بعد تمامها، فيتأخر عن الإعلال بناء على ما ذكره من أن الإعلال متقدم مما يعرض على الكلمة بعد تمامها.",
     "en": "Up to his statement “on the basis that the default in the noun is declension” — [herein lies the point] that declension too is among the accidents of the word after its completion, so it comes after iʿlāl, on the basis of what he mentioned: that iʿlāl precedes what befalls the word after its completion."},
]
