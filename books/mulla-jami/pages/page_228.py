# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 228 (printed ٢٢٧)."""

PAGE_NUMBER = 228
PRINTED_PAGE = "٢٢٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "بأقسامه الثلاثة، وواحد للمشتغل بالمتعلق، والأحسن في ترتيبها[[١]] حينئذ تأخير مثال المشتغل بالمتعلق، كما لا يخفى وجهه.",
     "en": "…in its three divisions, and one for [the verb] occupied with the dependent (mutaʿalliq); and the better arrangement of them would then be to put the example of [the verb] occupied with the dependent last, the reason for which is not hidden."},
    {"type": "matn",
     "ar": "(نحو: «زيدا ضربته») مثال الفعل المشتغل بالضمير مع تقدير تسليطه بعينه.",
     "en": "(As in: “Zayd, I struck him”—Zaydan ḍarabtuhu): an example of the verb occupied with the pronoun, with the verb itself supposed to be brought to bear [on the noun] (taslīṭ)."},
    {"type": "matn",
     "ar": "(و«زيدا مررت به») مثال الفعل المشتغل بالضمير مع تقدير تسليط ما يناسب بالترادف، فإن «مررت» بعد تعديته بالباء مرادف لـ«جاوزت».",
     "en": "(And “Zayd, I passed by him”—Zaydan marartu bihi): an example of the verb occupied with the pronoun, with what corresponds to it by synonymy supposed to be brought to bear; for “marartu,” once made transitive by the bāʾ, is synonymous with “jāwaztu” (I passed)."},
    {"type": "matn",
     "ar": "(و«زيدا ضربت غلامه») مثال الفعل المشتغل بالمتعلق.",
     "en": "(And “Zayd, I struck his servant”—Zaydan ḍarabtu ghulāmahu): an example of the verb occupied with the dependent."},
    {"type": "matn",
     "ar": "(و«زيدا حبست عليه») مثال الفعل المشتغل بالضمير مع تقدير تسليط ما يناسبه باللزوم، فإن حبس الشيء على الشيء يلزمه ملابسته للمحبوس عليه.",
     "en": "(And “Zayd, I was detained on his account”—Zaydan ḥubistu ʿalayhi): an example of the verb occupied with the pronoun, with what corresponds to it by entailment (luzūm) supposed to be brought to bear; for detaining a thing on account of a thing entails its being involved with the one on whose account it is detained."},
    {"type": "matn",
     "ar": "(وينصب) «زيد» في هذه الأمثلة (بفعل مضمر يفسره ما بعده[[٢]] أي: «ضربت») يعني: الفعل المفسر الناصب لـ«زيد» في «زيدا ضربته»: «ضربت» المقدر،",
     "en": "(And) “Zayd” in these examples (is put in the accusative by a suppressed verb that what follows it explains, namely “ḍarabtu”); he means: the explained verb that puts “Zayd” in the accusative in “Zaydan ḍarabtuhu” is the supposed “ḍarabtu,”"},
    {"type": "matn",
     "ar": "فإن الأصل فيه: «ضربت زيدا ضربته»[[٣]] أضمر «ضربت» الأول لوجود مفسره، أعني: «ضربت» الثاني.",
     "en": "for its underlying form is “ḍarabtu Zaydan ḍarabtuhu” (I struck Zayd, I struck him); the first “ḍarabtu” was suppressed because what explains it is present, namely the second “ḍarabtu.”"},
    {"type": "matn",
     "ar": "(و) على هذا القياس (جاوزت) فإنه مفسر بما يرادفه، أعني: «مررت به» (وأهنت)",
     "en": "(And) on this analogy (“jāwaztu”), for it is explained by what is synonymous with it, namely “marartu bihi”; (and “ahantu”)…"},

    {"type": "rule"},

    # ---------------- Footnote 8 of the previous page, continued ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "ومعمول الظاهر تفسيرا للمتعلق المقدر.",
     "en": "…and the object of the overt [verb] an explanation of the supposed dependent."},
    {"type": "pair",
     "ar": "وكذا جوز تقدير المجاوزة مع المتعلق في «زيدا مررت بغلامه».",
     "en": "Likewise, he allowed supposing [the verb of] passing together with the dependent in “Zaydan marartu bi-ghulāmihi” (Zayd, I passed by his servant)."},
    {"type": "pair",
     "ar": "وجوز أيضا فيما عدا الصورة الأولى تقدير فعل الملابسة.",
     "en": "He also allowed, in all but the first case, supposing a verb of involvement (mulābasa)."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وجهه الغير المخفي بمقتضى سوق كلامه خلوص أقسام المشتغل بالضمير عن الفصل بينها بما ليس منها.",
     "en": "Its unhidden reason, as the course of his discourse requires, is that the divisions of [the verb] occupied with the pronoun remain free of being separated from one another by what is not among them."},
    {"type": "pair",
     "ar": "وله وجه آخر وهو خلوص أمثلة المشتغل بالضمير عن الفصل بينها بما ليس منها.",
     "en": "It has another reason: that the examples of [the verb] occupied with the pronoun remain free of being separated from one another by what is not among them."},
    {"type": "pair",
     "ar": "ولما فعل المصنف أيضا وجهان حسنان:",
     "en": "What the author did also has two good reasons:"},
    {"type": "pair",
     "ar": "الأول: عدم الفصل بين الأفعال المعروفة بالفعل المجهول أعني: «حبست عليه».",
     "en": "First: not separating the active verbs by the passive verb, namely “ḥubistu ʿalayhi.”"},
    {"type": "pair",
     "ar": "والثاني: تقديم المسلط بنفسه، ثم المسلط بمرادفه، ثم المسلط باللازم إلا أنه قدم في هذا التقسيم ما هو أعرف فيه، تأمل.",
     "en": "Second: putting first [the verb] brought to bear by itself, then that brought to bear through its synonym, then that brought to bear through what it entails; except that in this division he put first what is better known in it. Reflect."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا بالمفسر كما ذهب إليه بعضهم.",
     "en": "Not by the explaining [verb], as some held."},
    {"type": "pair",
     "ar": "لا يخفى أن ما عدا الصورة الأولى يجوز أن يعد ما بعد الاسم المحدود ناصبا بتكلف بأن يقال: إنها سادة مسد أفعال صالحة لأن ينصبها، وفي قوتها أعني: جاوزت، وأهنت، ولابست.",
     "en": "It is not hidden that in all but the first case what follows the defined noun may be counted as putting it in the accusative, with some strain, by saying that these [verbs] stand in place of verbs fit to put it in the accusative and have their force, namely “jāwaztu,” “ahantu” and “lābastu.”"},
    {"type": "pair",
     "ar": "وأما الصورة الأولى: ففيها إشكال؛ إذ لا يجوز تعلق فعل طالب لمفعول واحد بمفعولين بالأصالة، فتعلقه بأحدهما بطريق التبعية بأن يكون أحدهما بدلا من الآخر،",
     "en": "As for the first case, there is a difficulty in it: a verb that requires one object cannot attach to two objects primarily, so it would attach to one of them by way of concord (tabaʿiyya), one of them being a substitute (badal) for the other."},
    {"type": "pair",
     "ar": "فإن كان الثاني بدلا من الأول لزم تعلق الفعل بالبدل قبل تعلقه بالمبدل منه مع لزوم الفصل بينهما بالجملة،",
     "en": "If the second is a substitute for the first, it follows that the verb attaches to the substitute before attaching to what it substitutes for, besides the necessary separation between them by the clause;"},
    {"type": "pair",
     "ar": "وإن كان الأول بدلا من الثاني لزم تقدم التابع على المتبوع مع لزوم الفصل بينهما بالجملة.",
     "en": "and if the first is a substitute for the second, it follows that the follower precedes what it follows, besides the necessary separation between them by the clause."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأولى أن يقال: فإن الأصل «ضربت زيدا» بترك «ضربته»، فإن في الأصل الفعل الأول موجود بدون الثاني،",
     "en": "It is better to say: “for the underlying form is ‘ḍarabtu Zaydan,’” leaving out “ḍarabtuhu”; for in the underlying form the first verb is present without the second,"},
    {"type": "pair",
     "ar": "وبعد حذفه احتيج إلى المفسر، ففسر بالثاني أو يقال: فإن التقدير: «ضربت زيدا ضربته».",
     "en": "and after its deletion an explaining [verb] was needed, so it was explained by the second; or to say: “for the supposed form (taqdīr) is ‘ḍarabtu Zaydan ḍarabtuhu.’”"},
]
