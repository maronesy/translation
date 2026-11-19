# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 592 (printed ٥٩١)."""

PAGE_NUMBER = 592
PRINTED_PAGE = "٥٩١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(لتأنيث المسند إليه) فاعلا» at the foot of PDF p. 591 (mid-sentence).
    {"type": "matn",
     "ar": "كان أو مفعول ما لم يسم فاعله.",
     "en": "…or the object of a verb whose agent is not named (mafʿūl mā lam yusamma fāʿiluhu)."},
    {"type": "matn",
     "ar": "وإنما جعلت هذه التاء ساكنة بخلاف تاء الاسم؛ لأن أصل الاسم الإعراب، وأصل الفعل البناء،",
     "en": "This tāʾ was made quiescent, unlike the tāʾ of the noun, because the default of the noun is inflection (iʿrāb) and the default of the verb is indeclinability (bināʾ);"},
    {"type": "matn",
     "ar": "فنبه من أول الأمر بسكون هذه على بناء ما لحقته، وبحركة تلك على إعراب ما وليته؛ لأنهما كالحرف الأخير مما تلحقانه.",
     "en": "so by the quiescence of this one it is signalled from the outset that what it is attached to is indeclinable, and by the vowel of that one that what it follows is inflected, since each of them is like the final letter of the word to which it is attached."},
    {"type": "matn",
     "ar": "(فإن كان) أي: المسند إليه[[١]] اسما (ظاهرا غير) مؤنث (حقيقي فمخير) أي: فأنت مخير بين إلحاق تاء التأنيث وبين عدمه،",
     "en": "(If it is), that is, the subject of predication, an (explicit) noun, (not) a (real) feminine, (then there is a choice), that is, you have the choice between attaching the tāʾ of the feminine and not attaching it;"},
    {"type": "matn",
     "ar": "أو فهو أي إلحاق تاء التأنيث مخير فيه على الحذف والإيصال[[٢]].",
     "en": "or: it, that is, attaching the tāʾ of the feminine, is something in which there is a choice, on the pattern of the omission [of the preposition] and the joining [of the verb directly] (al-ḥadhf wa-l-īṣāl)."},
    {"type": "matn",
     "ar": "وهذه المسألة قد تقدمت إلا أنها ذكرت[[٣]] فيما تقدم من حيث إنها من أحكام المؤنث، وهنا من حيث إنها من أحكام تاء التأنيث.",
     "en": "This question has come earlier, except that there it was mentioned as one of the rulings of the feminine, and here as one of the rulings of the tāʾ of the feminine."},
    {"type": "matn",
     "ar": "(وأما إلحاق علامة التثنية والجمعين) أي: جمعي المذكر والمؤنث في مثل: «قاما الزيدان، وقاموا الزيدون، وقمن النساء» (فضعيف)",
     "en": "(As for attaching the sign of the dual and of the two plurals), that is, the masculine and feminine plurals, in such cases as “qāmā l-Zaydāni, wa-qāmū l-Zaydūna, wa-qumna l-nisāʾu” (the two Zayds stood, the Zayds stood, the women stood), (it is weak),"},
    {"type": "matn",
     "ar": "لعدم احتياجها إلى هذه العلامات، مثل احتياج المسند إليه إلى علامة التأنيث؛",
     "en": "since it does not need these signs as the subject of predication needs the sign of the feminine;"},
    {"type": "matn",
     "ar": "لأن تأنيثه قد يكون معنويا أو سماعيا، وعلامة التثنية والجمع غالبا ظاهرة غاية الظهور.",
     "en": "for its feminine gender may be a matter of meaning or known only by usage (samāʿī), whereas the sign of the dual and the plural is, for the most part, entirely evident."},
    {"type": "matn",
     "ar": "وإذا ألحقت على ضعفها، فليست بضمائر؛ لئلا يلزم الإضمار قبل الذكر من غير فائدة،",
     "en": "When they are attached, weak as this is, they are not pronouns, lest there follow a pronoun before its mention (iḍmār qabla l-dhikr) without benefit;"},
    {"type": "matn",
     "ar": "بل هي حروف أتى بها للدلالة من أول الأمر على أحوال الفاعل، كتاء التأنيث.",
     "en": "rather, they are particles brought to indicate from the outset the states of the agent, like the tāʾ of the feminine."},
    {"type": "matn",
     "ar": "وفي شرح الرضي: هذا ما قاله النحاة، ولا منع من جعل هذه الحروف ضمائر، وإبدال الظاهر منها.",
     "en": "In the commentary of al-Raḍī: this is what the grammarians said; but nothing prevents making these letters pronouns, with the explicit noun as a substitute (badal) for them."},
    {"type": "matn",
     "ar": "والفائدة في مثل هذا الإبدال ما مر في بدل الكل من الكل، أو تكون الجملة خبر المبتدأ المؤخر، والغرض كون الخبر مهما.",
     "en": "The benefit of such substitution is what was given under the substitution of the whole for the whole (badal al-kull min al-kull); or the sentence is the predicate of a postponed subject, the purpose being that the predicate is of importance."},

    {"type": "section", "ar": "[التنوين]",
     "en": "Tanwīn"},

    {"type": "matn",
     "ar": "(التنوين) في الأصل مصدر «نونته» أي: أدخلته نونا، فسمي ما به ينون الشيء -",
     "en": "(Tanwīn) is originally the verbal noun of “nawwantuhu”, that is, “I gave it a nūn”; then that by which a thing is given a nūn was called…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أو المعنى، فإن كان تأنيث المسند إليه ظاهرا غير حقيقي",
     "en": "Or the meaning is: “if the feminine gender of the subject of predication is explicit and not real”;"},
    {"type": "pair",
     "ar": "أو المعنى، فإن كان المسند إليه المؤنث ظاهرا غير حقيقي.",
     "en": "or the meaning is: “if the feminine subject of predication is explicit and not real”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "والأولى جعله اسم مكان.",
     "en": "It is better to take it [mukhayyar] as a noun of place."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وبهذا لا يندفع كون ذكرها مستغنى عنه،",
     "en": "This does not dispel [the objection] that mentioning it [again] is superfluous;"},
    {"type": "pair",
     "ar": "فالوجه أن يقال: المتبادر من قوله: وتلحق الوجوب، فاستثنى منه الظاهر الغير الحقيقي.",
     "en": "so the right answer is to say: what first comes to mind from his words “and it is attached” is obligation, so he excepted from it the explicit non-real [feminine]."},
]
