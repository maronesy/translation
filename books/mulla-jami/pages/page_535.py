# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 535 (printed ٥٣٤)."""

PAGE_NUMBER = 535
PRINTED_PAGE = "٥٣٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «والباء زائدة لازمة إلا إذا» at the foot of PDF p. 534 (mid-sentence).
    {"type": "matn",
     "ar": "كان المتعجب منه «أن» مع صلتها نحو: «أحسن أن يقول» أي: بأن يقول، على ما هو القياس",
     "en": "…the object of wonder is “an” with its relative clause, as in “aḥsin an yaqūla” (how well he speaks!), that is, bi-an yaqūla, in accordance with the analogical rule;"},
    {"type": "matn",
     "ar": "(فلا ضمير) عند سيبويه (في «أفعل»)؛ لأن الفاعل واحد ليس إلا.",
     "en": "(so there is no pronoun), according to Sībawayh, (in “afʿil”), because the agent is one only."},
    {"type": "matn",
     "ar": "(و«به») أي: مجروره (ومفعول عند الأخفش) لـ«أحسن»، بمعنى: «صر ذا حسن»، على أن يكون همزة الفعل للصيرورة",
     "en": "(And “bihi”), that is, what it governs in the genitive, (is an object, according to al-Akhfash), of “aḥsin” in the sense of “become possessed of beauty”, on the view that the hamza of the verb is for becoming (ṣayrūra);"},
    {"type": "matn",
     "ar": "(والباء للتعدية) أي: لجعل اللازم متعديا، فالمعنى: «صيره ذا حسن»",
     "en": "(and the bāʾ is for transitivization), that is, for making the intransitive transitive; so the meaning is: “make him possessed of beauty”;"},
    {"type": "matn",
     "ar": "(أو) الباء (زائدة) على أن يكون «أحسن» متعديا بنفسه، ويكون همزة «أحسن» للتعدية كـ«أخرج»",
     "en": "(or) the bāʾ is (redundant), on the view that “aḥsin” is transitive by itself and the hamza of “aḥsin” is for transitivization, as in “akhrij” (bring out);"},
    {"type": "matn",
     "ar": "(ففيه) أي: في أفعل (ضمير هو فاعله) أي: «أحسن أنت[[١]] بزيد أو زيدا» أي: اجعله حسنا؛ بمعنى: صفه به.",
     "en": "(so in it), that is, in afʿil, (there is a pronoun which is its agent), that is, “aḥsin anta bi-Zaydin” or “Zaydan”, that is, make him beautiful, in the sense of: describe him with it."},
    {"type": "matn",
     "ar": "وقال الفراء وتبعه الزمخشري: إن «أحسن» أمر لكل واحد بأن يجعل زيدا حسنا،",
     "en": "Al-Farrāʾ said, and al-Zamakhsharī followed him, that “aḥsin” is a command to everyone to make Zayd beautiful;"},
    {"type": "matn",
     "ar": "وإنما يجعله كذلك بأن يصفه بالحسن فكأنه قيل: صفه بالحسن كيف شئت، فإن فيه من جهات الحسن كل ما يمكن أن يكون في شخص.",
     "en": "and one makes him so only by describing him with beauty; so it is as though it were said: “describe him with beauty however you wish, for there is in him, of the aspects of beauty, everything that can be in a person.”"},

    {"type": "section", "ar": "[أفعال المدح والذم]",
     "en": "The Verbs of Praise and Blame"},

    # REVIEW: printed «إحداهما» (dual) although four variants follow, and no preceding statement such as «وفيهما أربع لغات» is printed after the heading; transcribed as printed.
    {"type": "matn",
     "ar": "إحداهما: «فعل» بفتح الفاء وكسر العين، وهي الأصل.",
     "en": "The first of them: “faʿila”, with fatḥa on the fāʾ and kasra on the ʿayn; this is the original form."},
    {"type": "matn",
     "ar": "والثانية: «فعل» بإسكان العين مع فتح الفاء.",
     "en": "The second: “faʿl”, with the ʿayn quiescent and fatḥa on the fāʾ."},
    {"type": "matn",
     "ar": "والثالثة: إسكان العين مع كسر الفاء.",
     "en": "The third: the ʿayn quiescent with kasra on the fāʾ."},
    # REVIEW: printed «اتباعا» (hamzat al-waṣl) for the expected «إتباعا»; transcribed as printed.
    {"type": "matn",
     "ar": "والرابعة: كسر الفاء اتباعا للعين،",
     "en": "The fourth: kasra on the fāʾ in harmony with the ʿayn (itbāʿ)."},
    {"type": "matn",
     "ar": "والأكثر في هذين الفعلين عند بني تميم إذا قصد بهما المدح والذم كسر الفاء وإسكان العين.",
     "en": "Most common in these two verbs among the Banū Tamīm, when praise and blame are intended by them, is kasra on the fāʾ and a quiescent ʿayn."},
    {"type": "matn",
     "ar": "قال سيبويه: وكأن عامة العرب اتفقوا على لغة بني تميم.",
     "en": "Sībawayh said: it is as though the generality of the Arabs agreed on the dialect of the Banū Tamīm."},
    {"type": "matn",
     "ar": "(وشرطهما[[٢]]) أي: شرط «نعم وبئس» (أن يكون الفاعل معرفا باللام) للعهد الذهني،",
     "en": "(And their condition), that is, the condition of “niʿma and biʾsa”, (is that the agent be made definite by the lām) of mental reference (al-ʿahd al-dhihnī);"},
    {"type": "matn",
     "ar": "وهي لواحد غير معين ابتداء، ويصير معينا بذكر المخصوص بعده،",
     "en": "it refers at the outset to an unspecified individual, and becomes specified by the mention of the specified term (al-makhṣūṣ) after it;"},
    {"type": "matn",
     "ar": "ويكون في الكلام تفصيل بعد الإجمال؛ ليكون أوقع[[٣]] في النفس نحو: «نعم الرجل زيد» (أو)",
     "en": "so there is in the speech detail after summary, so that it may be more impressive on the soul, as in “niʿma al-rajulu Zaydun” (an excellent man is Zayd), (or)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الخطاب لمن يتوجه إليه الكلام بتأويل المخاطب، ولذا لا يتصرف فيه بتأنيث الفعل وتثنيته وجمعه.",
     "en": "The address is to whoever the speech is directed at, by interpreting [it as] “the addressee”; for this reason the verb is not modified in it by making it feminine, dual or plural."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أشار إلى أن ورود فاعلهما نكرة، نحو: نعم رجل زيد، أو مضافا إلى النكرة، نحو: نعم صاحب قوم لا سلاح لهم قليل ملحق بالعدم.",
     "en": "He indicated that the occurrence of their agent as indefinite, as in “niʿma rajulun Zaydun”, or annexed to an indefinite, as in “niʿma ṣāḥibu qawmin lā silāḥa lahum” (an excellent companion of a people who have no weapons), is rare and treated as non-existent."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: إنما اختير التفصيل بعد الإبهام، ولم يفصل ابتداء ليكون أوقع لشوق النفس إلى معرفة المبهم، ولصيرورته مذكورا مرتين،",
     "en": "That is: detail after vagueness was chosen, and it was not detailed at the outset, only so that it may be more impressive, because of the soul’s longing to know the vague, and because of its coming to be mentioned twice;"},
    {"type": "pair",
     "ar": "والمقام يقتضي الأوقعية؛ لأن المدح العام مما يستبعد وقوعه، وهذا ظاهر إلا أن هذا غير مختص بالفاعل المعرف باللام.",
     "en": "and the context requires greater impressiveness, because general praise is something whose occurrence is deemed unlikely. This is evident, except that this is not peculiar to the agent made definite by the lām."},
]
