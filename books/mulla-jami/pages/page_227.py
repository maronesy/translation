# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 227 (printed ٢٢٦)."""

PAGE_NUMBER = 227
PRINTED_PAGE = "٢٢٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "رفع ذلك الاشتغال (عليه) أي: على ذلك الاسم (هو) أي: أحد الأمرين الفعل أو شبهه بعينه",
     "en": "…upon the removal of that preoccupation, (over it), that is, over that noun, (it), that is, one of the two, the verb or what resembles it, itself,"},
    {"type": "matn",
     "ar": "(أو مناسبه[[١]]) أي: ما يناسبه بالترادف[[٢]] أو اللزوم",
     "en": "(or what corresponds to it), that is, what corresponds to it by synonymy or by entailment,"},
    {"type": "matn",
     "ar": "(لنصبه) أي: لنصب أحد هذين الأمرين الاسم بالمفعولية؛ كما هو الظاهر المتبادر[[٣]].",
     "en": "(it would put it in the accusative), that is, one of these two would put the noun in the accusative as an object, as is the evident and immediate sense."},
    {"type": "matn",
     "ar": "فبقيد الاشتغال[[٤]] بالضمير أو متعلقه خرج نحو: «زيدا ضربت».",
     "en": "By the restriction “preoccupation with the pronoun or what is connected with it,” the like of “Zaydan ḍarabtu” (Zayd I struck) is excluded."},
    {"type": "matn",
     "ar": "وبقيد الفراغ عن العمل فيه بمجرد الاشتغال خرج نحو: «زيد ضربته»،",
     "en": "By the restriction “free of governing it merely through the preoccupation,” the like of “Zaydun ḍarabtuhu” (Zayd, I struck him) is excluded;"},
    {"type": "matn",
     "ar": "فإن المانع من عمل «ضربته» في «زيد» ليس مجرد اشتغاله بضميره، فإن زيدا عمل معنى الابتداء فيه ورفعه إياه أيضا مانع عن ذلك.",
     "en": "for what prevents “ḍarabtuhu” from governing “Zayd” is not merely its preoccupation with his pronoun: the governance of the abstract notion of inception (maʿnā al-ibtidāʾ) in “Zayd,” and its putting it in the nominative, also prevents that."},
    {"type": "matn",
     "ar": "وبقيد النصب بالمفعولية خرج خبر «كان» في نحو: «زيدا كنت إياه»[[٥]].",
     "en": "By the restriction “the accusative as an object,” the predicate of “kāna” is excluded, as in “Zaydan kuntu iyyāhu” (Zayd, I was he)."},
    {"type": "matn",
     "ar": "وههنا صور أربع:",
     "en": "There are four cases here:"},
    {"type": "matn",
     "ar": "إحداها: اشتغال الفعل بالضمير مع تقدير تسليطه بعينه.",
     "en": "The first: the verb is preoccupied with the pronoun, and it is itself supposed to be given power [over the noun]."},
    {"type": "matn",
     "ar": "والثانية: اشتغاله بالضمير مع تقدير تسليط ما يناسب الفعل بالترادف[[٦]].",
     "en": "The second: it is preoccupied with the pronoun, and what corresponds to the verb by synonymy is supposed to be given power."},
    {"type": "matn",
     "ar": "والثالثة: اشتغال الفعل بالضمير مع تقدير تسليط ما يناسب الفعل باللزوم[[٧]].",
     "en": "The third: the verb is preoccupied with the pronoun, and what corresponds to the verb by entailment is supposed to be given power."},
    {"type": "matn",
     "ar": "والرابعة: اشتغال الفعل بالمتعلق، ولا يتصور حينئذ إلا تقدير تسليط الفعل المناسب باللزوم[[٨]]،",
     "en": "The fourth: the verb is preoccupied with what is connected [with the noun]; in that case only the supposition that a verb corresponding by entailment is given power can be conceived."},
    {"type": "matn",
     "ar": "ولهذا أورد المصنف أربعة أمثلة، ثلاثة منها للمشتغل بالضمير",
     "en": "For this reason the author gave four examples, three of them for [the verb] preoccupied with the pronoun…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ليس في أكثر النسخ، بل في شيء من كتبه، وإنما ألحقه غيره ليدخل فيه الأمثلة الأخيرة.",
     "en": "It is not in most copies, nor in any of his books; someone else added it so that the last examples would be included."},
    {"type": "pair",
     "ar": "ويمكن أن يعني: بتسليطه تسليطه بعينه أو بلازمه، فلا حاجة في دخولها إلى الإلحاق.",
     "en": "He may mean by “its being given power” its being given power itself or through what it entails; then there is no need of the addition for them to be included."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: فيه مساهلة؛ لأن الترادف في المفردات لا غير،",
     "en": "It has been said: this is loose wording, because synonymy holds only between single words."},
    {"type": "pair",
     "ar": "وفيه بحث؛ لأن العامل مجرد الفعل أو شبهه لا المركب وهو مفرد.",
     "en": "This is open to discussion, because the governor is the verb or what resembles it alone, not the compound, and that is a single word."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "متعلق بجميع أمور اعتبرها في كلام المتن لا بمجرد قوله: بالمفعولية.",
     "en": "[This] attaches to all the matters he took into account in the text of the matn, not merely to his words “as an object.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "شروع في بيان فوائد القيود المذكورة في الحد.",
     "en": "He begins explaining the purposes of the restrictions mentioned in the definition."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ولا يخفى أنه خرج خبر كان بقوله: كل اسم؛",
     "en": "It is evident that the predicate of “kāna” is already excluded by his words “every noun,”"},
    {"type": "pair",
     "ar": "لأنه كما أن المتبادر في هذا المقام من قوله: لنصب النصب بالمفعولية كذلك المتبادر من كل اسم المفعول،",
     "en": "because, just as what is immediately understood here from his words “it would put it in the accusative” is the accusative as an object, so what is immediately understood from “every noun” is the object."},
    {"type": "pair",
     "ar": "ولك أن تقول: كل اسم أعم من المفعول، والتعريف لمطلق ما أضمر عامله على شريطة التفسير، ومنه «زيدا كنت إياه»،",
     "en": "You may say: “every noun” is more general than the object, and the definition is of whatever has its governor suppressed on condition of explanation, which includes “Zaydan kuntu iyyāhu”;"},
    {"type": "pair",
     "ar": "فلا معنى لتقييد قوله: لنصبه لإخراجه.",
     "en": "so there is no sense in restricting his words “it would put it in the accusative” in order to exclude it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه مساهلة لأن الترادف إنما يكون في المفردات.",
     "en": "This is loose wording, because synonymy holds only between single words."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "ولو بواسطة كما إذا توالت أسماء منصوبات بمقدرات نحو: «زيدا أخاه غلامه ضربته» أي: لابست زيدا أهنت أخاه ضربت غلامه.",
     "en": "Even through an intermediary, as when several nouns follow one another in the accusative through supplied verbs, as in “Zaydan akhāhu ghulāmahu ḍarabtuhu,” that is: “I had to do with Zayd, I humiliated his brother, I struck his servant.”"},

    # ---------------- Footnote 8 (continues on p.228) ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وجوز الشيخ الرضي في هذا القسم تقدير نفس الفعل مع تقدير متعلقه،",
     "en": "Shaykh al-Raḍī allowed, in this kind, supplying the verb itself together with supplying what is connected with it;"},
    {"type": "pair",
     "ar": "فتقول في «زيدا ضربت غلامه»: أن التقدير «ضربت» متعلق «زيد ضربت غلامه»، فيكون الفعل الظاهر تفسيرا للفعل المقدر،",
     "en": "so you say of “Zaydan ḍarabtu ghulāmahu” that the implied form is “I struck what is connected with Zayd, I struck his servant,” so that the explicit verb is an explanation of the supplied verb…"},
]
