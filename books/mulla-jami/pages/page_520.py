# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 520 (printed ٥١٩)."""

PAGE_NUMBER = 520
PRINTED_PAGE = "٥١٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فمعنى «صار» الانتقال،» at the foot of PDF p. 519 (mid-sentence).
    {"type": "matn",
     "ar": "وحكم معناه أي: أثره المترتب عليه كون الخبر منتقلا إليه،",
     "en": "…and the effect of its meaning, that is, its consequence that follows from it, is the predicate’s being what is transitioned to."},
    {"type": "matn",
     "ar": "فلما دخل على الجملة الاسمية أعني: «زيد غني» وأفاد حكم معناه الذي هو الانتقال، أعطي الخبر وهو «غني» أثر ذلك الانتقال، وهو كون الغني منتقلا إليه.",
     "en": "So when it entered upon the nominal sentence, namely “zaydun ghaniyyun” (Zayd is rich), and conveyed the effect of its meaning, which is transition, the predicate, “ghaniyy”, was given the consequence of that transition, which is riches being what is transitioned to."},
    {"type": "matn",
     "ar": "(فترفع) هذه الأفعال الجزء (الأول) لكونه فاعلا[[١]] (وتنصب) الجزء (الثاني) لشبهه بالمفعول به في توقف الفعل عليه[[٢]] (مثل: «كان زيد قائما»).",
     "en": "(So they put in the nominative), these verbs, the (first) part, because it is an agent, (and put in the accusative) the (second) part, because of its resemblance to the direct object in that the verb depends on it, (as in “kāna zaydun qāʾiman” (Zayd was standing))."},
    {"type": "matn",
     "ar": "(فـ«كان» تكون ناقصة[[٣]]) كائنة (لثبوت خبرها[[٤]] لاسمها) ثبوتا (ماضيا[[٥]]) أي: كائنا في الزمان الماضي",
     "en": "(So “kāna” is defective), being (for the establishment of its predicate for its subject) — an establishment (in the past), that is, occurring in past time —"},
    {"type": "matn",
     "ar": "(دائما) من غير دلالة على عدم سابق أو انقطاع لاحق نحو: «كان زيد فاضلا»",
     "en": "(permanently), without indicating a prior non-existence or a subsequent cessation, as in “kāna zaydun fāḍilan” (Zayd was virtuous),"},
    {"type": "matn",
     "ar": "(أو منقطعا) نحو: «كان زيد غنيا فافتقر»",
     "en": "(or interrupted), as in “kāna zaydun ghaniyyan fa-ftaqara” (Zayd was rich and then became poor);"},
    # REVIEW: printed «كان يكون ناقصة» (masculine يكون, against «تكون» elsewhere); transcribed as printed.
    {"type": "matn",
     "ar": "(وبمعنى «صار») عطف على قوله: «لثبوت خبرها» أي: كان يكون ناقصة كائنة بمعنى: صار،",
     "en": "(and in the sense of “ṣāra”): coordinated with his words “for the establishment of its predicate”, that is, kāna is defective, being in the sense of ṣāra;"},
    # REVIEW: printed «كقوله الشاعر» (pronoun suffix plus الشاعر); transcribed as printed.
    {"type": "matn",
     "ar": "فهو من قبيل عطف أحد القسمين على الآخر لا على ما هو قسم منه، كقوله الشاعر:",
     "en": "so it is of the type of coordinating one of the two divisions with the other, not with what is a division of it; as in the poet’s saying:"},
    {"type": "verse",
     "ar": "بتيهاء قفر[[٦]] والمطي كأنها     قطا الحزن قد كانت فراخا بيوضها",
     "en": "In a trackless, empty waste, while the riding camels were like the sandgrouse of the rugged ground whose eggs had become chicks."},
    {"type": "matn",
     "ar": "أي: صارت فراخا بيوضها، فإن بيوضها لم تكن فراخا، بل صارت[[٧]] فراخا",
     "en": "That is, its eggs had become chicks; for its eggs had not been chicks, but had become chicks."},
    {"type": "matn",
     "ar": "(ويكون فيها ضمير الشأن) هذا أيضا عطف على قوله: «للثبوت» أي: «كان» تكون ناقصة يكون فيها ضمير الشأن اسما لها، والجملة الواقعة بعدها خبرا لها مفسرا للضمير، كقوله:",
     "en": "(And the pronoun of the matter (ḍamīr al-shaʾn) may be in it): this too is coordinated with his words “for the establishment”, that is, “kāna” is defective with the pronoun of the matter in it as its subject, and the sentence that occurs after it as its predicate, explaining the pronoun; as in his saying:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: اصطلاحيا بناء على أن الفعل لا بد له من فاعل لفظي، ولذا لم يعد المصنف اسمها في المرفوعات على حدة.",
     "en": "That is, [an agent] in the technical sense, on the basis that a verb must have an agent in wording; hence the author did not count its subject separately among the nominatives."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: كما أن الفعل المتعدي لا يتم معناه بدون المفعول به لا تتم معاني هذه الأفعال بدون أخبارها.",
     "en": "He means: just as the meaning of a transitive verb is not complete without the direct object, so the meanings of these verbs are not complete without their predicates."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "تفصيل لبيان المعاني التي يمتاز بها بعض هذه الأفعال عن بعض بعد ما ذكر القدر المشترك بينها المميز عما سواها.",
     "en": "A detailed exposition of the meanings by which some of these verbs are distinguished from others, after he mentioned the measure shared among them that distinguishes them from everything else."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "جعل الجار والمجرور ظرفا مستقرا ليصح عطف قوله: ويكون فيها ضمير الشأن عليه،",
     "en": "He made the preposition and its object a stable adverbial (ẓarf mustaqarr), so that the coordination of his words “and the pronoun of the matter may be in it” with it would be sound;"},
    {"type": "pair",
     "ar": "وهو حال كما يقتضيه الذوق السليم. ويجوز أن يكون صفة، وأن يكون خبرا بعد خبر.",
     "en": "it is a circumstantial, as sound taste requires. It may also be an attribute, or a second predicate."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الأولى جعل ماضيا مفعولا فيه أي: في زمان ماض، وتنكيره لبيان أنه ليس لزمان معين من الماضي.",
     "en": "It is better to make “māḍiyan” an adverb of time (mafʿūl fīhi), that is, “in a past time”; its indefiniteness shows that it is not for a specific time in the past."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "التيهاء: المفازة التي لا يهتدي فيها من التيه بمعنى الضلالة.",
     "en": "Al-tayhāʾ is the desert in which one finds no way, from al-tīh in the sense of going astray."},
    {"type": "pair",
     "ar": "والقفر: المكان الخالي يصف المطي بسرعة سيرها،",
     "en": "Al-qafr is the empty place. He describes the riding camels by the speed of their going:"},
    {"type": "pair",
     "ar": "فإنها بمنزلة قطا تركت بيوضا صارت فراخا، فهي تمشي بسرعة إلى فراخها، كذا في العباب.",
     "en": "they are like sandgrouse that left eggs which have become chicks, so they go swiftly to their chicks. So [it is] in al-ʿUbāb."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: انتقلت إلى الفراخة من البيوضة، وهو معنى مقصود من الكلام، فتكون بمعنى صار لا زائدة،",
     "en": "That is, they passed from being eggs to being chicks; and this is a meaning intended by the speech, so it is in the sense of ṣāra, not redundant;"},
    {"type": "pair",
     "ar": "ومن لم يتدبر توهم أن البيان ناقص.",
     "en": "whoever has not reflected has imagined that the explanation is deficient."},
]
