# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 564 (printed ٥٦٣)."""

PAGE_NUMBER = 564
PRINTED_PAGE = "٥٦٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «متمسكين بقول الشاعر:» at the foot of PDF p. 563.
    {"type": "verse",
     "ar": "تالله ربك إن قتلت لمسلما          وجبت عليك عقوبة المتعمد",
     "en": "…“By God your Lord, you have indeed killed a Muslim; the punishment of the wilful [killer] has become binding upon you.”"},
    {"type": "matn",
     "ar": "وهو شاذ عند البصريين.",
     "en": "This is anomalous (shādhdh) according to the Baṣrans."},
    # REVIEW: the full stop after «وإعمال المكسورة» is printed so, though the sentence runs on («بعد تخفيفها في سعة الكلام واقع»); transcribed as printed.
    {"type": "matn",
     "ar": "(وتخفف المفتوحة) كالمكسورة (فتعمل) عند التخفيف على سبيل الوجوب (في ضمير شأن مقدر) والسبب في تقديره: إن مشابهة المفتوحة بالفعل أكثر[[١]] من مشابهته المكسورة به، كما سبق[[٢]]،",
     "en": "(And the open [anna] is lightened), like the broken [inna], (and then it governs), when lightened, necessarily, (an implied pronoun of the matter (ḍamīr al-shaʾn)). The reason for implying it is that the resemblance of the open [anna] to the verb is greater than the resemblance of the broken [inna] to it, as has preceded;"},
    {"type": "matn",
     "ar": "وإعمال المكسورة. بعد تخفيفها في سعة الكلام واقع، كقوله تعالى: ﴿وإن كلا لما ليوفينهم﴾[[٣]]،",
     "en": "and the governing of the broken [inna] after its lightening occurs in the ordinary range of speech (saʿat al-kalām), as in His words, the Exalted: “And indeed (wa-in) to each your Lord will fully repay them”;"},
    {"type": "matn",
     "ar": "وإعمال المفتوحة بعد تخفيفها لم يقع في سعة الكلام، ويلزم منه بحسب الظاهر[[٤]] ترجيح الأضعف على الأقوى، وذلك غير جائز،",
     "en": "whereas the governing of the open [anna] after its lightening has not occurred in the ordinary range of speech. From this there follows, on the face of it, the preference of the weaker over the stronger, and that is not permissible."},
    {"type": "matn",
     "ar": "فقدروا ضمير الشأن[[٥]] حتى يكون اسما للمفتوحة بعد تخفيفها، والجملة المفسرة لضمير الشأن خبرا لها، فتكون عاملا في المبتدأ والخبر، كما كانت في الأصل.",
     "en": "So they implied the pronoun of the matter, so that it is the noun (ism) of the open [anna] after its lightening, and the clause explicating the pronoun of the matter is its predicate (khabar); thus it governs the mubtadaʾ and the khabar, as it did originally."},
    {"type": "matn",
     "ar": "فهي لا تزال عاملا، بخلاف المكسورة، فإنها قد تكون عاملا، وقد لا تكون.",
     "en": "So it never ceases to govern, unlike the broken [inna], which sometimes governs and sometimes does not."},
    {"type": "matn",
     "ar": "والعمل في الظاهر وإن كان أقوى من العمل في المقدر، لكن دوام العمل في المقدر يقاوم العمل في الظاهر في وقت دون وقت، فلا يلزم ترجيح الأضعف على الأقوى.",
     "en": "Governing an explicit [noun], even if it is stronger than governing an implied one, is nevertheless matched by permanent governing of the implied, against governing the explicit at one time and not another; so the preference of the weaker over the stronger does not follow."},
    {"type": "matn",
     "ar": "(فتدخل) أي: المفتوحة (على الجمل) الصالحة لأن تكون مفسرة لضمير الشأن (مطلقا)، سواء كانت اسمية أو فعلية[[٦]]، وداخلا فعلها على المبتدأ والخبر أو غير داخل.",
     "en": "(So it enters), that is, the open [anna], (upon clauses) fit to explicate the pronoun of the matter, (without restriction), whether they are nominal or verbal, and whether their verb enters upon a mubtadaʾ and khabar or does not."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال المصنف في أمالي المسائل المتفرقة: التشبيه في أن المفتوحة من حيث اللفظ والمعنى والاستعمال.",
     "en": "The author (al-muṣannif) said in Amālī al-masāʾil al-mutafarriqa: the likeness [to the verb] in the open anna is in respect of wording, meaning and usage."},
    {"type": "pair",
     "ar": "أما اللفظ فلأنها مفتوحة الأول كالماضي. وأما المعنى: فلأنها تغير معنى الجملة كالفعل.",
     "en": "As for wording, it is because its first [letter] carries a fatḥa, like the past-tense verb (māḍī). As for meaning, it is because it alters the meaning of the clause, like the verb."},
    {"type": "pair",
     "ar": "وأما الاستعمال فهو أن العرب عطفت على محل اسم \"إن\" المكسورة، ولم تعطف على محل اسم المفتوحة كما لا تعطف على معمول الفعل.",
     "en": "As for usage, it is that the Arabs coordinated upon the syntactic position (maḥall) of the noun of the broken “inna”, but did not coordinate upon the position of the noun of the open [anna], just as they do not coordinate upon what a verb governs."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "في بحث ضمير الشأن، لكن المذكور فيه أن المفتوحة أقوى مشابهة من المكسورة، ولم يذكر فيه دليله، فالحوالة لا طائل تحتها.",
     "en": "In the discussion of the pronoun of the matter; but what is stated there is only that the open [anna] has a stronger resemblance than the broken, and its proof is not given there, so the cross-reference is of no use."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة هود: ١١١.",
     "en": "Qurʾān, Sūrat Hūd 11:111."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وأما بحسب الحقيقة، فلا ترجيح للأضعف على الأقوى؛ لأن الأقوى مغير للمعنى دون الأضعف.",
     "en": "As for the reality of the matter, there is no preference of the weaker over the stronger, because the stronger alters the meaning and the weaker does not."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأنه بحسب تقدير المعمول تكون الجملة بعد تقديره كما كانت قبله، وما ذلك إلا ضمير الشأن.",
     "en": "Because, by implying the governed term, the clause after its implication remains as it was before it; and that is only the pronoun of the matter."},
    {"type": "pair",
     "ar": "وقيل: لا يلزم كون اسمها ضمير الشأن.",
     "en": "It has also been said that its noun need not be the pronoun of the matter."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إذا لم يدخل عليها نواسخ المبتدأ، فلا بد أن تكون جملة اسمية، وإذا دخلت عليها جاز كونها فعلية أيضا.",
     "en": "When the abrogators of the mubtadaʾ (nawāsikh al-mubtadaʾ) do not enter upon it, it must be a nominal clause; when they do enter upon it, it may also be verbal."},
]
