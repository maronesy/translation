# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 413 (printed ٤١٢)."""

PAGE_NUMBER = 413
PRINTED_PAGE = "٤١٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «...بخلاف «متى» فإنه غير مختص بهما، والمشهور فتح» at the foot of PDF p. 412.
    {"type": "matn",
     "ar": "الهمزة والنون، وقد جاء كسرهما أيضا.",
     "en": "…of the hamza and the nūn; their being given kasra has also occurred."},
    {"type": "matn",
     "ar": "(و) منها: («كيف») الكائنة (للحال استفهاما) أي: حال الشيء وصفته، فالمراد بالحال صفة الشيء لا زمان الحال كما توهمه بعض الشارحين.",
     "en": "(And) among them is (“kayfa”), which is (for state, interrogatively), that is, the state of a thing and its attribute; what is meant by “state” is the attribute of the thing, not present time, as some commentators supposed."},
    {"type": "matn",
     "ar": "قال صاحب المفصل: و«كيف» جار مجرى الظروف، ومعناه السؤال عن الحال، تقول: «كيف زيد؟» أي: على أي حال هو.",
     "en": "The author of al-Mufaṣṣal said: “kayfa” is treated like the adverbs, and its meaning is asking about the state; you say “kayfa Zaydun?” (how is Zayd?), that is, in what state is he?"},
    {"type": "matn",
     "ar": "ويستعمل للشرط مع «ما» على ضعف عند البصريين، نحو: «كيفما تجلس أجلس»، أي: على أي هيئة تجلس أجلس، ومطلقا عند الكوفيين نحو: «كيف تجلس أجلس»،",
     "en": "It is used for condition with “mā”, weakly, according to the Baṣrans, as in “kayfamā tajlis ajlis” (however you sit, I shall sit), that is, in whatever posture you sit, I shall sit; and without restriction according to the Kūfans, as in “kayfa tajlis ajlis”."},
    {"type": "matn",
     "ar": "فإن كان بعده اسم فهو في محل الرفع بالخبرية[[١]] عنه، وإن كان بعده فعل مثل: «كيف جئت؟» فهو في محل النصب على الحالية[[٢]]، أي: على أي حال جئت أراكبا أو ماشيا؟",
     "en": "If a noun follows it, it is in the position of the nominative as the khabar of it; and if a verb follows it, as in “kayfa jiʾta?” (how did you come?), it is in the position of the accusative as a ḥāl, that is, in what state did you come, riding or walking?"},
    {"type": "matn",
     "ar": "(ومنها) أي: من الظروف المبنية («مذ» و«منذ»[[٣]]) وإنما بنيتا لموافقتهما[[٤]] «مذ ومنذ» الحرفين.",
     "en": "(And among them), that is, among the indeclinable adverbs, are (“mudh” and “mundhu”); they are indeclinable only because they coincide with the particles “mudh” and “mundhu”."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إذ لم يدخل ناسخ الابتداء على ذلك الاسم وإن دخل نحو: «كيف أصبحت؟ وكيف تعلم زيدا؟» فـ«كيف» منصوب المحل خبرا أو مفعولا ثانيا لتلك الناسخ، كذا في الرضي.",
     "en": "When no annuller of the subject–predicate construction (nāsikh) has entered that noun; if one has entered, as in “kayfa aṣbaḥta?” (how did you fare this morning?) and “kayfa taʿlamu Zaydan?” (how do you know Zayd to be?), then “kayfa” is accusative in position, as the khabar or as the second object of that annuller; so in al-Raḍī."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ويجوز أن يكون منصوب المحل صفة للمصدر الذي تضمنه ذلك الفعل، فكان معنى كيف يقوم زيد؟ يقوم زيد قياما حاصلا على أي صفة.",
     "en": "It may also be accusative in position as a qualifier of the maṣdar contained in that verb; so the meaning of “kayfa yaqūmu Zaydun?” would be “Zayd stands with a standing occurring in what manner?”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: إنهما كلمتان برأسهما؛ إذ الأصل في الحرف وما يشبهه عدم التصرف.",
     "en": "It has been said that they are two independent words, since the default in a particle and what resembles it is the absence of inflection."},
    {"type": "pair",
     "ar": "وقيل: أصل «مذ منذ» بدليل «منيذ»، وإنه يضم الذال لالتقاء الساكنين.",
     "en": "It has also been said that the origin of “mudh” is “mundhu”, as shown by [the diminutive] “munaydh”, and that the dhāl takes ḍamma because of the meeting of two quiescent letters."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قال الرضي: الأخفش والحجازيون يجرون بهما مطلقا، والكوفيون: يرفعون بهما مطلقا،",
     "en": "Al-Raḍī said: al-Akhfash and the Ḥijāzīs put [what follows] in the genitive with them without restriction, and the Kūfans put it in the nominative with them without restriction."},
    {"type": "pair",
     "ar": "وأكثر العرب يجرون بهما في الزمان الحاضر اتفاقا، وإنما الخلاف بينهم في الجر بهما في الزمان الماضي، ولا يستعملان في المستقبل اتفاقا.",
     "en": "Most Arabs use the genitive with them for present time, by agreement; the disagreement among them is only over the genitive with them for past time; and by agreement they are not used for the future."},
    {"type": "pair",
     "ar": "وإذا جر بهما فقيل: إنهما اسمان مضافان، والصحيح أنهما حرفا جر بمعنى «من» لابتداء الغاية إذا كان الزمان ماضيا معرفة نحو: «ما رأيته مذ اليوم»",
     "en": "When the genitive is used with them, it has been said that they are annexed nouns; the correct view is that they are prepositions, in the sense of “min” for the starting point, when the time is past and definite, as in “mā raʾaytuhu mudh al-yawmi” (I have not seen him since the day);"},
    # REVIEW: the definite-past example printed is «ما رأيته مذ اليوم» and the present example «ما رأيته مذ الليلة»; transcribed as printed.
    {"type": "pair",
     "ar": "وبمعنى «في» إن كان حاضرا معرفة نحو: «ما رأيته مذ الليلة»، وبمعنى «من وإلى» جميعا، فيدخلان على الزمان الذي وقع فيه ابتداء الفعل وانتهاؤه. وذلك إذا كان الزمان نكرة نحو: «ما رأيته مذ أربعة أيام»،",
     "en": "in the sense of “fī” if it is present and definite, as in “mā raʾaytuhu mudh al-laylati” (I have not seen him this night); and in the sense of both “min” and “ilā”, so that they enter on the time in which the action began and ended; that is when the time is indefinite, as in “mā raʾaytuhu mudh arbaʿati ayyāmin” (I have not seen him for four days)."},
    {"type": "pair",
     "ar": "ثم إن المصنف ذكر في بنائهما ثلاثة أوجه: الأول: في شرح الكافية: وهو أنه وضع «مذ» وضع الحرف، وحمل «منذ» عليه لاتفاقهما في المعنى.",
     "en": "The author [Ibn al-Ḥājib] gave three reasons for their indeclinability. The first, in Sharḥ al-Kāfiya: that “mudh” is coined as particles are coined, and “mundhu” is assimilated to it because they agree in meaning."},
    {"type": "pair",
     "ar": "والثاني: ما في شرح المفصل: وهو ما ذكره في الشرح.",
     "en": "The second is what is in Sharḥ al-Mufaṣṣal, namely what [the commentator] mentioned in the commentary."},
    {"type": "pair",
     "ar": "والثالث: ما ذكره فيهما: وهو أنها مقطوعة الإضافة مرادة في المعنى. ولذلك بنيت «منذ» على الضم كما بني ما قطع عن الإضافة،",
     "en": "The third is what he mentioned in both: that it is cut off from annexation, [the annexation] being intended in meaning; for this reason “mundhu” is indeclinable with ḍamma, as what is cut off from annexation is indeclinable."},
    {"type": "pair",
     "ar": "ألا ترى أن قولك: «منذ يوم الجمعة»، معناه: أول المدة فهو يتضمن المضاف إليه كتضمن قبل عند القطع إلا أنه لم يأت إلا مبنيا؛ لأنه لم يذكر المضاف إليه معه أبدا بخلاف قبل.",
     "en": "Do you not see that your saying “mundhu yawmi al-jumuʿati” (since Friday) means “the beginning of the period”? So it contains the annexed noun, as “qabl” does when cut off; except that it has only ever occurred as indeclinable, because the annexed noun is never mentioned with it, unlike “qabl”."},
]
