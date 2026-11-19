# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 306 (printed ٣٠٥)."""

PAGE_NUMBER = 306
PRINTED_PAGE = "٣٠٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإن زيدا ليس» from the foot of PDF p. 305.
    {"type": "matn",
     "ar": "جنسا للغلام صادقا عليه ولا ظرفه، فإضافة الغلام إليه بمعنى اللام أي: «غلام لزيد».",
     "en": "…a genus of “slave” predicable of it, nor its container; so the annexation of “slave” to him is in the sense of the lām, that is, “a slave belonging to Zayd.”"},
    {"type": "matn",
     "ar": "(وإما بمعنى «من») البيانية (في جنس المضاف) الصادق عليه وعلى غيره،",
     "en": "(Or in the sense of) the explicative (“min,” in the genus of the muḍāf), which is predicable of it and of other things,"},
    {"type": "matn",
     "ar": "بشرط أن يكون المضاف أيضا[[١]] صادقا على غير المضاف إليه، فيكون بينهما عموم وخصوص من وجه.",
     "en": "on condition that the muḍāf too be predicable of things other than the muḍāf ilayhi, so that between the two there is a relation of partial overlap (ʿumūm wa-khuṣūṣ min wajh)."},
    {"type": "matn",
     "ar": "(وإما بمعنى «في» في ظرفه) أي: ظرف المضاف.",
     "en": "(Or in the sense of “fī,” in its container), that is, the container of the muḍāf."},
    {"type": "matn",
     "ar": "والحاصل[[٢]]: أن المضاف إليه: إما مباين للمضاف، وحينئذ إن كان ظرفا له، فالإضافة بمعنى «في»، وإلا فهي بمعنى «اللام»،",
     "en": "The upshot is that the muḍāf ilayhi is either disjoint from the muḍāf; and in that case, if it is a container for it, the annexation is in the sense of “fī,” and otherwise it is in the sense of the lām;"},
    {"type": "matn",
     "ar": "وإما مساو[[٣]] له كـ«ليث وأسد»، أو أعم مطلقا كـ«أحد اليوم»[[٤]]؛ فالإضافة على التقديرين ممتنعة.",
     "en": "or it is equal to it in extension, as with “layth” and “asad” (both “lion”), or more general without qualification, as in “aḥadu l-yawmi” (the Sunday of the day); on both suppositions the annexation is impossible."},
    {"type": "matn",
     "ar": "وإما أخص مطلقا كـ«يوم الأحد، وعلم الفقه، وشجر الأراك»، فالإضافة حينئذ أيضا بمعنى اللام،",
     "en": "Or it is more specific without qualification, as in “yawmu l-aḥadi” (Sunday), “ʿilmu l-fiqhi” (the science of jurisprudence) and “shajaru l-arāki” (the arāk tree); in that case too the annexation is in the sense of the lām."},
    {"type": "matn",
     "ar": "وإما أخص من وجه، فإن كان المضاف إليه أصلا للمضاف، فالإضافة بمعنى «من»، وإلا فهي أيضا بمعنى «اللام»،",
     "en": "Or it is more specific in one respect: then, if the muḍāf ilayhi is the material origin of the muḍāf, the annexation is in the sense of “min,” and otherwise it too is in the sense of the lām."},
    {"type": "matn",
     "ar": "فإضافة «خاتم» إلى «فضة» بيانية، وإضافة «فضة» إلى «خاتم» بمعنى اللام، كما يقال: «فضة خاتمك خير من فضة خاتمي».",
     "en": "So the annexation of “khātam” (ring) to “fiḍḍa” (silver) is explicative, and the annexation of “fiḍḍa” to “khātam” is in the sense of the lām, as when one says: “the silver of your ring is better than the silver of my ring.”"},
    {"type": "matn",
     "ar": "واعلم أنه لا يلزم فيما هو بمعنى اللام أن يصح التصريح بها بل يكفي إفادة الاختصاص الذي هو مدلول اللام،",
     "en": "Know that in what is in the sense of the lām it is not required that the lām may be stated explicitly; it suffices that it convey the specificity (ikhtiṣāṣ) that the lām signifies."},
    {"type": "matn",
     "ar": "فقولك: «يوم الأحد، وعلم الفقه، وشجر الأراك»[[٥]] بمعنى «اللام»، ولا يصح إظهار «اللام» فيه[[٦]]،",
     "en": "So your saying “yawmu l-aḥadi,” “ʿilmu l-fiqhi” and “shajaru l-arāki” is in the sense of the lām, though the lām cannot be made explicit in it."},
    {"type": "matn",
     "ar": "وبهذا الأصل يرتفع الإشكال عن كثير من مواد الإضافة اللامية، ولا يحتاج فيه إلى التكلفات[[٧]] البعيدة مثل: «كل رجل وكل واحد».",
     "en": "By this principle the difficulty is removed from many instances of lām-annexation, and there is no need in them for far-fetched contrivances, as with “kullu rajulin” (every man) and “kullu wāḥidin” (every one)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا حاجة إلى ذكر هذا الشرط؛ لأنه إذا صدق المضاف إليه على المضاف وغيره لا محالة يصدق المضاف على غير المضاف إليه لامتناع إضافة الأخص مطلقا.",
     "en": "There is no need to mention this condition, for if the muḍāf ilayhi is predicable of the muḍāf and of other things, the muḍāf is necessarily predicable of things other than the muḍāf ilayhi, since annexation of the absolutely more specific is impossible."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: حاصل البيان في هذا المقام.",
     "en": "That is, the upshot of the exposition in this place."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كأن المراد بالمساواة المساواة الشاملة للمرادفة والمساواة.",
     "en": "It is as if what is meant by equality (musāwāt) is the equality that includes synonymy and equality [of extension]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فإن الأحد هو يوم الأحد.",
     "en": "For al-aḥad is Sunday (yawm al-aḥad)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الأنسب بحسب المعنى أن يكون هذه الإضافات بيانية، وإظهار من فيها خال من التكلف إلا أن أئمة العربية جعلوها لامية، ولا يظهر ما دعاهم إليه،",
     "en": "What is more suitable in meaning is that these annexations be explicative, and making “min” explicit in them is free of strain; but the authorities of Arabic made them lām-annexations, and what led them to this is not apparent."},
    {"type": "pair",
     "ar": "وكذا كل رجل، فالأظهر فيه أن يكون الإضافة بمعنى «من»، أي: كل هو رجل،",
     "en": "Likewise “kullu rajulin”: the more evident view is that the annexation in it is in the sense of “min,” that is, “every [one] that is a man”;"},
    {"type": "pair",
     "ar": "وصح حمل المفرد على كل مع أنه متعدد؛ لأنه متناول للمتعدد على سبيل البدل.",
     "en": "and predicating the singular of “kull,” though it is plural, is sound, because [the singular] covers the plural by way of alternation (ʿalā sabīl al-badal)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إذ لم يستعمل يوم للأحد. وكذا الحال في الباقيتين، وفي مسجد الجامع، وطور سيناء، والأسماء اللازمة الإضافة مثل عند وذو ولدى.",
     "en": "For “yawmun li-l-aḥadi” is not used. The case is the same in the remaining two, and in “masjidu l-jāmiʿi” (the mosque of the congregation), “ṭūru sīnāʾa” (Mount Sinai), and the nouns that are always annexed, such as “ʿinda,” “dhū” and “ladā.”"},
    # REVIEW: print reads «يتسعمل» (letters transposed); «يستعمل» is meant; transcribed as printed.
    {"type": "pair",
     "ar": "ولما لم يتسعمل مقطوعة، فإذا قطعت أوجب تنافرا لأنه غير مأنوس.",
     "en": "Since they are not used cut off [from annexation], when they are cut off this produces dissonance (tanāfur), because it is unfamiliar."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قيل في تصحيح إضافة كل إلى رجل: إن كلا لإحاطة جزئيات كلي أضيف هو إليه.",
     "en": "It has been said, to justify annexing “kull” to “rajul”: “kull” is for encompassing the particulars of the universal to which it is annexed."},
    {"type": "pair",
     "ar": "وإضافة الجزئي إلى الكلي بمعنى اللام، لكن يمتنع إظهار اللام إلا بعد التأويل بالجزئيات أو الأفراد مثلا، وإلا لزم",
     "en": "The annexation of the particular to the universal is in the sense of the lām, but making the lām explicit is impossible except after interpreting [it] as “the particulars” or “the individuals,” for example; otherwise there would follow…"},
]
