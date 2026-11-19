# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 341 (printed ٣٤٠)."""

PAGE_NUMBER = 341
PRINTED_PAGE = "٣٤٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإن المعطوف» at the foot of PDF p. 340.
    {"type": "matn",
     "ar": "فيها ليس في حكم المعطوف عليه.",
     "en": "…does not, in these, have the status of the noun conjoined to."},
    {"type": "matn",
     "ar": "وإنما قلنا: «بشرط ألا يكون ما يقتضيها منتفيا في المعطوف» احترازا عن مثل قولنا: «يا رجل والحارث»،",
     "en": "We said “provided that what requires them is not absent in the conjoined noun” only to exclude such as our saying “yā rajulu wa-l-Ḥārith” (O man, and al-Ḥārith!);"},
    {"type": "matn",
     "ar": "فإن «الحارث» معطوف على «الرجل» وليس في حكمه من حيث تجرده عن اللام، فإن ما يقتضي تجرده عن اللام هو اجتماع اللام وحرف النداء، وهو مفقود في المعطوف،",
     "en": "for “al-Ḥārith” is conjoined to “rajul” but does not share its status with respect to its being bare of the article, since what requires its being bare of the article is the combination of the article with the vocative particle, and that is absent in the conjoined noun."},
    {"type": "matn",
     "ar": "وأما نحو: «رب شاة وسخلتها» فبتقدير التنكير لقصد عدم التعيين[[١]] أي: «رب شاة وسخلة لها»،",
     "en": "As for such as “rubba shātin wa-sakhlatihā” (many a ewe and its lamb), it is by supposing indefiniteness, to intend non-specification, that is, “rubba shātin wa-sakhlatin lahā” (many a ewe and a lamb of hers);"},
    {"type": "matn",
     "ar": "أو محمول[[٢]] على نكارة الضمير كـ«ربه رجلا» على الشذوذ أي: «رب شاة وسخلة شاة»،",
     "en": "or it is construed on the indefiniteness of the pronoun, as in “rubbahu rajulan” (many a one, a man), as an anomaly (shudhūdh), that is, “rubba shātin wa-sakhlati shātin” (many a ewe and a ewe’s lamb)."},
    {"type": "matn",
     "ar": "وكذا المعطوف في حكم المعطوف عليه في أحوال عارضة له بالنظر إلى نفسه وغيره، إن كان المعطوف مثل المعطوف عليه،",
     "en": "Likewise, the conjoined noun has the status of the noun conjoined to in states that befall it with regard to itself and to something else, if the conjoined noun is like the noun conjoined to."},
    {"type": "matn",
     "ar": "فلذا وجب بناء المعطوف في «يا زيد وعمرو»؛ لأن ضم «زيد» بالنظر إلى حرف النداء وإلى كونه مفردا معرفة في نفسه، و«عمرو» مثل «زيد» في كونه مفردا معرفة،",
     "en": "Hence the conjoined noun is necessarily indeclinable in “yā Zaydu wa-ʿAmru” (O Zayd and ʿAmr!), because the ḍamma of “Zayd” is with regard to the vocative particle and to its being in itself a singular definite noun, and “ʿAmr” is like “Zayd” in being singular and definite;"},
    {"type": "matn",
     "ar": "وامتنع بناؤه في «يا زيد وعبد الله»، فإن «عبد الله» ليس مثل «زيد»، فإن «زيدا» مفرد معرفة، و«عبد الله» مضاف.",
     "en": "and its indeclinability is barred in “yā Zaydu wa-ʿAbda llāhi” (O Zayd and ʿAbd Allāh!), for “ʿAbd Allāh” is not like “Zayd”: “Zayd” is a singular definite noun, while “ʿAbd Allāh” is annexed."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل أن المعطوف في حكم المعطوف عليه فيما يجوز ويمتنع",
     "en": "(Hence), that is, because the conjoined noun has the status of the noun conjoined to in what is permitted and barred,"},
    {"type": "matn",
     "ar": "(لم يجز في) تركيب مثل («ما زيد بقائم -أو قائما-، ولا ذاهب عمرو» إلا الرفع) في «ذاهب»؛",
     "en": "(nothing is permitted in) a construction such as (“mā Zaydun bi-qāʾimin—or qāʾiman—wa-lā dhāhibun ʿAmrun” [Zayd is not standing, nor is ʿAmr going] except the nominative) in “dhāhib”;"},
    {"type": "matn",
     "ar": "إذ لو نصب أو خفض[[٣]] لكان معطوفا على «قائم» أو «قائما»، فيكون خبرا عن «زيد»،",
     "en": "for were it put in the accusative or the genitive, it would be conjoined to “qāʾim” or “qāʾiman”, and would thus be a predicate of “Zayd”;"},
    {"type": "matn",
     "ar": "وهو ممتنع لخلوه عن الضمير الواقع في المعطوف عليه العائد إلى اسم «ما»،",
     "en": "and that is barred, because it lacks the pronoun present in the noun conjoined to, which refers back to the noun of “mā”."},
    {"type": "matn",
     "ar": "فتعين الرفع على أن يكون[[٤]] خبرا مقدما لمبتدأ، وهو «عمرو»[[٥]]، ويكون من قبيل عطف الجملة على الجملة، ولا مانع منه.",
     "en": "So the nominative is required, on the basis that it is a predicate placed before its subject (mubtadaʾ), namely “ʿAmr”; and it is then a case of conjoining a sentence to a sentence, to which there is no impediment."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بناء على أن الإضافة للعهد الذهني.",
     "en": "On the basis that the annexation is for mental reference (al-ʿahd al-dhihnī)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "اعلم أنهم جعلوا الحمل على نكارة الضمير جوابا والشذوذ جوابا آخر.",
     "en": "Know that they made construal on the indefiniteness of the pronoun one answer and anomaly another answer."},
    {"type": "pair",
     "ar": "واعترض عليه بأن الضمير إنما يكون نكرة إذا لم يكن له مرجع كضمير «ربه رجلا».",
     "en": "It has been objected that a pronoun is indefinite only when it has no referent, like the pronoun of “rubbahu rajulan”."},
    {"type": "pair",
     "ar": "ويمكن أن يجاب عنه: بأن ذلك مبني على ما ذهب إليه الشيخ الرضي من أن الضمائر الراجعة إلى النكرات إذا لم تكن تلك النكرات مختصة بحكم وصفة كانت نكرات.",
     "en": "It may be answered that this rests on the view of Shaykh al-Raḍī that pronouns referring to indefinite nouns are themselves indefinite when those indefinite nouns are not specified by a ruling or a qualifier."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ولا يجوز أن يكون معطوفا على قائما وعمرو معطوفا على زيد حتى يكون من باب العطف على معمولي عامل واحد لامتناع عمل ما في الخبر المتقدم.",
     "en": "It cannot be conjoined to “qāʾiman” with “ʿAmr” conjoined to “Zayd”, so as to be a case of conjunction to the two governed words of a single governor, because “mā” cannot govern a predicate placed first."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يحتمل أن يكون مبتدأ، وعمرو فاعله.",
     "en": "It may be a subject (mubtadaʾ), with “ʿAmr” as its agent."},
    {"type": "pair",
     "ar": "وإنما لم يذكر هذا الاحتمال لأنه حينئذ في قوة الفعلية، فيصير بمنزلة عطف الفعلية على الاسمية.",
     "en": "He did not mention this possibility only because it would then have the force of a verbal sentence, and so would amount to conjoining a verbal sentence to a nominal one."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ولقائل أن يقول: لم يتعين لذلك لجواز أن يكون الرفع لكونه مبتدأ رافعا للفاعل وهو عمرو؛ لأن الصفة إذا طابقت مفردا جاز فيه الأمران.",
     "en": "One might say: it is not required for that reason, since the nominative may be due to its being a subject that puts its agent, namely “ʿAmr”, in the nominative; for when the qualifier agrees with a singular noun, both [analyses] are permitted in it."},
]
