# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 463 (printed ٤٦٢)."""

PAGE_NUMBER = 463
PRINTED_PAGE = "٤٦٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… بالوجوه الثلاثة (الحسن وجه)» at the foot of PDF p. 462.
    {"type": "matn",
     "ar": "أيضا بهذه الوجوه.",
     "en": "…also in these ways."},
    {"type": "matn",
     "ar": "وإنما قدم الصفة الكائنة باللام في أول تقسيم المسائل على الصفة المجردة عن اللام؛ لأن مفهوم الأول وجودي والثاني عدمي،",
     "en": "He put the adjective with the lām before the adjective devoid of the lām at the start of the division of the cases because the concept of the first is positive (wujūdī) and that of the second privative (ʿadamī);"},
    {"type": "matn",
     "ar": "وعكس الترتيب في تفصيلها؛ لأن أقسام الصفة المجردة أشرف؛ لأن قسما واحدا منها مختلف فيه، وسائر الأقسام صحيح بخلاف أقسام ذات اللام.",
     "en": "and he reversed the order in their detailed exposition because the divisions of the bare adjective are nobler, since one division of them is disputed and the remaining divisions are sound, unlike the divisions of the adjective with the lām."},
    {"type": "matn",
     "ar": "فإن قسمين منها ممتنع كما قال (اثنان منها) أي: من تلك الأقسام (ممتنعان):",
     "en": "For two divisions of those are impossible, as he said: (two of them), that is, of those divisions, (are impossible):"},
    {"type": "matn",
     "ar": "أحدهما: الصفة باللام[[١]] مضافة إلى معمولها المضاف إلى ضمير الموصوف بواسطة أو غير واسطة، (مثل: الحسن وجهه) و«الحسن وجه غلامه»،",
     "en": "The first of them: the adjective with the lām annexed to its governed term which is itself annexed to the pronoun of the qualified noun, directly or indirectly, (as in “al-ḥasanu wajhihi”) and “al-ḥasanu wajhi ghulāmihi”;"},
    {"type": "matn",
     "ar": "لعدم إفادة الإضافة فيه خفة؛ لأن الخفة في الصفة المشبهة: إما بحذف التنوين أو النون كـ«حسن وجهه» بالإضافة،",
     "en": "because annexation yields no lightness in it; for lightness in the resembling adjective is either by dropping the tanwīn or the nūn, as in “ḥasanu wajhihi” with annexation;"},
    {"type": "matn",
     "ar": "أو بحذف ضمير الموصوف من فاعل الصفة، أو مما أضيف إليه الفاعل، واستتاره في الصفة مثل: «الحسن الوجه» و«الحسن وجه الغلام»،",
     "en": "or by dropping the pronoun of the qualified noun from the agent of the adjective, or from that to which the agent is annexed, and concealing it in the adjective, as in “al-ḥasanu l-wajh” and “al-ḥasanu wajhi l-ghulām”;"},
    {"type": "matn",
     "ar": "أو بحذفهما معا، ولا خفة فيه بواحد منها[[٢]].",
     "en": "or by dropping both together; and there is no lightness in it by any one of these."},
    {"type": "matn",
     "ar": "وثانيهما: أن تكون الصفة باللام مضافة إلى معمولها المجرد عن اللام، (مثل: «الحسن وجه») أو «وجه غلام»؛",
     "en": "The second of them: that the adjective with the lām be annexed to its governed term devoid of the lām, (as in “al-ḥasanu wajhin”) or “wajhi ghulāmin”;"},
    {"type": "matn",
     "ar": "لأن إضافة «الحسن» إلى «وجه» وإن أفادت التخفيف بحذف الضمير واستتاره في الصفة، لكنهم لم يجوزوها؛",
     "en": "because the annexation of “al-ḥasan” to “wajh”, although it yields lightening by dropping the pronoun and concealing it in the adjective, they nevertheless did not permit it;"},
    {"type": "matn",
     "ar": "لأن إضافة المعرفة إلى النكرة وإن كانت لفظية مفيدة للتخفيف، لكنها في الصورة تشبه عكس المعهود من الإضافة[[٣]].",
     "en": "because the annexation of a definite to an indefinite, even if it is verbal and yields lightening, in form resembles the reverse of what is usual in annexation."},
    {"type": "matn",
     "ar": "(واختلف في) صورة كانت الصفة فيها مجردة عن اللام مضافة إلى معمولها المضاف إلى ضمير الموصوف (مثل: «حسن وجهه»)",
     "en": "(There is disagreement over) the configuration in which the adjective is devoid of the lām and annexed to its governed term, which is annexed to the pronoun of the qualified noun, (as in “ḥasanu wajhihi”):"},
    {"type": "matn",
     "ar": "فسيبويه وجميع البصريين يجوزونها على قبح في ضرورة الشعر، والكوفيون يجوزونها بلا قبح في السعة.",
     "en": "Sībawayh and all the Baṣrans permit it, as unseemly, under poetic necessity, while the Kūfans permit it without unseemliness in ordinary usage."},
    {"type": "matn",
     "ar": "وجه الاستقباح: أنهم إنما ارتكبوا الإضافة لقصد التخفيف، فيقتضي الحال أن يبلغ إلى أقصى ما يمكن منه، ويقبح أن يقتصر على أهون التخفيفين، أعني: حذف",
     "en": "The ground for deeming it unseemly is that they resorted to annexation only to aim at lightening, so the situation requires that it reach the utmost possible degree of it, and it is unseemly to stop at the lesser of the two lightenings, namely the omission of…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: المفردة بدليل أن جميع الأمثلة من المفردات.",
     "en": "That is, the singular one, as shown by all the examples being singulars."},
    {"type": "pair",
     "ar": "وأما المثنى نحو: الزيدان حسنا وجهاهما، والمجموع نحو الزيدون حسنوا وجوههم، فهو مما اختلفوا فيه كما في حسن وجهه، كما يجيء في الرضي.",
     "en": "As for the dual, as in “al-Zaydāni ḥasanā wajhayhimā”, and the plural, as in “al-Zaydūna ḥasanū wujūhihim”, it is among what they disagreed over, as with “ḥasanu wajhihi”, as comes in al-Raḍī."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأن التنوين سقط باللام، والضمير في وجهه موجود.",
     "en": "Because the tanwīn has already fallen away through the lām, and the pronoun in “wajhihi” is present."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: الإضافة المعنوية، فإن المعهود فيها إضافة النكرة إلى المعرفة؛ إذ لا تفيد فيها،",
     "en": "That is, semantic annexation; for what is usual in it is the annexation of the indefinite to the definite, since [the converse] yields nothing in it;"},
    {"type": "pair",
     "ar": "فكذا الإضافة اللفظية؛ لأنها فرعها، فلا تخالفها من كل وجه.",
     "en": "and so too verbal annexation, because it is its branch, so it does not differ from it in every respect."},
]
