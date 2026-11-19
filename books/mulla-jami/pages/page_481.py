# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 481 (printed ٤٨٠)."""

PAGE_NUMBER = 481
PRINTED_PAGE = "٤٨٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… من غير حاجة إلى» at the foot of PDF p. 480 (mid-sentence).
    {"type": "matn",
     "ar": "ضم كلمة أخرى إليها لاستقلاله[[١]] بالمفهومية.",
     "en": "…joining another word to it, because [the meaning] is independent in being understood (mafhūmiyya)."},
    {"type": "matn",
     "ar": "ويمكن إرجاع الضمير «في نفسه» إلى المعنى، وحينئذ يكون المراد[[٢]] بكون المعنى في نفسه: استقلاله بالمفهومية،",
     "en": "The pronoun in “fī nafsihi” may also be referred back to the meaning; in that case what is meant by the meaning’s being in itself is its independence in being understood."},
    {"type": "matn",
     "ar": "فمرجع[[٣]] كون المعنى في نفسه، وكونه في نفس الكلمة إلى أمر واحد، وهو استقلاله بالمفهومية،",
     "en": "So the meaning’s being in itself and its being in the word itself come back to one thing, namely its independence in being understood;"},
    {"type": "matn",
     "ar": "لكن[[٤]] المطابق لما ذكر في وجه الحصر إرجاع الضمير إلى «ما دل»، كما لا يخفى.",
     "en": "but what accords with what was stated in the account of the restriction is referring the pronoun back to “mā dalla”, as is evident."},
    {"type": "matn",
     "ar": "اعلم أن الفعل مشتمل على ثلاثة معان[[٥]]:",
     "en": "Know that the verb comprises three meanings:"},
    {"type": "matn",
     "ar": "أحدها: الحدث الذي هو بمعنى المصدر.",
     "en": "First: the event (ḥadath), which has the sense of the verbal noun (maṣdar)."},
    {"type": "matn",
     "ar": "وثانيها: الزمان.",
     "en": "Second: time."},
    {"type": "matn",
     "ar": "وثالثها: النسبة إلى فاعل ما.",
     "en": "Third: the attribution to some agent."},
    {"type": "matn",
     "ar": "ولا شك أن النسبة إلى فاعل ما معنى حرفي، هو آلة لملاحظة طرفيها، فلا يستقل بالمفهومية[[٦]].",
     "en": "There is no doubt that the attribution to some agent is a particle-like meaning (maʿnā ḥarfī), an instrument for regarding its two terms, so it is not independent in being understood."},
    {"type": "matn",
     "ar": "فالمراد بـ«معنى في نفسه» ليس تلك النسبة.",
     "en": "So what is meant by “a meaning in itself” is not that attribution."},
    {"type": "matn",
     "ar": "ولما وصف ذلك المعنى بالاقتران بالزمان تعين أن يكون المراد به الحدث[[٧]].",
     "en": "And since he described that meaning as being conjoined with time, it is determined that what is meant by it is the event."},
    {"type": "matn",
     "ar": "فالمراد بالمعنى: ليس معناه المطابقي[[٨]]، بل أعم[[٩]]، لكن لا يتحقق إلا في ضمن التضمني.",
     "en": "So what is meant by “meaning” is not its full-correspondence meaning (al-maʿnā al-muṭābiqī), but something more general, which, however, is realized only within the implicated (taḍammunī) meaning."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لكونه حاصلا في الذهن منفردا لعدم كونه آلة لملاحظة الغير، ومرآة لتعرف حاله.",
     "en": "Because it is present in the mind on its own, since it is not an instrument for regarding something else, nor a mirror for knowing that thing’s state."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأن كون الشيء في نفسه كناية عن استقلاله، وعدم احتياجه إلى الغير،",
     "en": "For a thing’s being in itself is an allusion to its independence and its not needing anything else;"},
    {"type": "pair",
     "ar": "ولما وصف المعنى أي: المفهوم الحاصل في الذهن به يكون المراد منه استقلاله بالمفهومية.",
     "en": "and since the meaning, that is, the concept present in the mind, is described by it, what is meant by it is its independence in being understood."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "مصدر ميمي لكون خبره الجار والمجرور.",
     "en": "[Marjiʿ is] a mīm-verbal noun (maṣdar mīmī), since its predicate is the prepositional phrase."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "استدراك لدفع توهم ناشيء من كون مآلهما إلى أمر واحد، وهو أنه كيف رجح الوجه الأول ومآله إلى الثاني.",
     "en": "A qualification (istidrāk) to remove a misapprehension arising from the two coming back to one thing, namely: how could he prefer the first reading when it comes back to the second?"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هذا هو المشهور فيما بين القوم.",
     "en": "This is the well-known view among the scholars."},
    {"type": "pair",
     "ar": "والتحقيق أنه مشتمل على أربعة معان: رابعها: تقييد الحدث، أو النسبة بالزمان، وهو أيضا معنى حرفي غير مستقل.",
     "en": "The verified view is that it comprises four meanings, the fourth being the restriction of the event, or of the attribution, by time; and this too is a particle-like meaning, not independent."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إذ لا تفهم النسبة ما لم تفهم الذات المنسوب إليها الحدث.",
     "en": "Since the attribution is not understood so long as the entity to which the event is attributed is not understood."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "إذ لا يمكن إرادة الزمان؛ إذ لا معنى لاقتران الشيء بنفسه،",
     "en": "Since time cannot be meant, for a thing’s being conjoined with itself has no sense;"},
    {"type": "pair",
     "ar": "والمراد بضمير «به» لفظ المعنى بدون الوصفين.",
     "en": "and what is meant by the pronoun in “bihi” is the word “meaning” without the two qualifications."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لعدم الاستقلال بالمفهومية لكون جزئه، وهو النسبة غير مستقلة،",
     "en": "Because it is not independent in being understood, since a part of it, namely the attribution, is not independent;"},
    {"type": "pair",
     "ar": "فتوصيفه بقوله: في نفسه مانع عن إرادته، وإن كان المتبادر المعنى المطابقي.",
     "en": "so his qualifying it by “in itself” prevents it from being meant, even though what first comes to mind is the full-correspondence meaning."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "إذ لا قرينة على الخصوص، وليكون لفظ المعنى في تعاريف الأقسام الثلاثة على نسق واحد.",
     "en": "Since there is no contextual indicator of specificity, and so that the word “meaning” in the definitions of the three divisions follows one pattern."},
]
