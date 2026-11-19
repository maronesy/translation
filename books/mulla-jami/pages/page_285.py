# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 285 (printed ٢٨٤)."""

PAGE_NUMBER = 285
PRINTED_PAGE = "٢٨٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «عملا بالمختار على» from the foot of PDF p. 284.
    {"type": "matn",
     "ar": "قدر الإمكان (مثل: «ما جاءني من أحد[[١]] إلا زيد») فـ«زيد» بدل مرفوع محمول على موضع «أحد» لا مجرور محمول على لفظه",
     "en": "…as far as possible, (as in “Not anyone came to me except Zayd”): “Zayd” is a substitute (badal) in the nominative, carried on the position of “aḥad,” not in the genitive carried on its wording;"},
    {"type": "matn",
     "ar": "(و) مثل: («لا أحد فيها») أي: في الدار (إلا عمرو») فـ«عمرو» مرفوع ومحمول على محل «أحد» لا على لفظه",
     "en": "(and) as in (“There is no one in it”), that is, in the house, (“except ʿAmr”): “ʿAmr” is nominative and carried on the place (maḥall) of “aḥad,” not on its wording;"},
    {"type": "matn",
     "ar": "(و) مثل: («ما زيد شيئا إلا شيء لا يعبأ به») أي: لا يعتد به، فـ«شيء» مرفوع محمول على محل «شيئا» لا منصوب على لفظه،",
     "en": "(and) as in (“Zayd is not anything except a thing of no account”), that is, not taken into reckoning: “shayʾun” is nominative, carried on the place of “shayʾan,” not accusative on its wording."},
    {"type": "matn",
     "ar": "وقوله: «لا يعبأ به» ليس في كثير من النسخ، وعلى ما وقع في بعضها فهو صفة «شيء» المستثنى.",
     "en": "His words “of no account” are not in many of the copies; on the reading found in some of them, it is an attribute of the excepted “shayʾ.”"},
    {"type": "matn",
     "ar": "قيل: إنما وصفه به[[٢]] لئلا يلزم استثناء الشيء من نفسه،",
     "en": "It has been said: he qualified it by this only so that it would not follow that a thing is excepted from itself."},
    {"type": "matn",
     "ar": "ولا يخفى أنه لو جعل المستثنى منه شيئا أعم من أن يزيد عليه صفة غير الشيئية أو لا، وخص المستثنى بما لا يزيد عليه صفة غير الشيئية لكان أدق وألطف.",
     "en": "It is not hidden that had the excepted-from (mustathnā minhu) been made a thing more general than whether some attribute other than thingness (shayʾiyya) is added to it or not, and the excepted (mustathnā) been restricted to that to which no attribute other than thingness is added, it would have been more precise and more subtle."},
    {"type": "matn",
     "ar": "وإنما تعذر البدل على اللفظ في صورة الأولى (لأن «من») الاستغراقية[[٣]] (لا تزاد) اتفاقا (بعد الإثبات) أي: بعد ما صار الكلام مثبتا لانتقاض النفي بـ«إلا»؛",
     "en": "The substitute on the wording is precluded in the first case only (because the) all-inclusive (istighrāqī) (“min” is not added), by agreement, (after an affirmation), that is, after the sentence has become affirmative through the negation being broken by “illā”;"},
    {"type": "matn",
     "ar": "لأنها لتأكيد النفي[[٤]]، ولا نفي بعد الانتقاض بـ«إلا»،",
     "en": "for it serves to reinforce the negation, and there is no negation after it has been broken by “illā.”"},
    {"type": "matn",
     "ar": "فلو أبدل على اللفظ وقيل: «ما جاءني من أحد إلا زيد» بالجر كان في قوة قولنا: «جاءني من زيد»، فلزم زيادة «من» في الإثبات، وذلك غير جائز.",
     "en": "So if the substitute were made on the wording, and one said “Not anyone came to me except Zaydin” in the genitive, it would be equivalent to our saying “There came to me min Zayd,” and the addition of “min” in an affirmative would follow; and that is not permitted."},
    {"type": "matn",
     "ar": "وفي الصورتين الأخيرتين: لأنه لو أبدل المستثنى على اللفظ، وقيل: «لا أحد فيها إلا عمرا[[٥]]» بالنصب؛",
     "en": "In the last two cases [it is precluded] because, if the excepted were made a substitute on the wording, and one said “There is no one in it except ʿAmran” in the accusative—"},
    {"type": "matn",
     "ar": "لأن فتحته شبيهة بالحركة الإعرابية؛ لأنها حصلت بكلمة «لا»، فهي كالنصب الحاصل بالعامل،",
     "en": "since its fatḥa resembles an inflectional vowel, because it arose through the word “lā,” and so is like the accusative produced by a governor (ʿāmil)—"},
    {"type": "matn",
     "ar": "فلا بد حينئذ من تقدير «لا» حقيقة أو حكما؛ ليعمل فيه هذا العمل،",
     "en": "then “lā” would have to be supposed, really or virtually, so as to exert this government on it."},
    {"type": "matn",
     "ar": "وكذا في قوله: «ما زيد شيئا إلا شيء» لو حمل المستثنى على لفظ المستثنى منه لا بد حينئذ من تقدير «ما» كذلك ليعمل فيه",
     "en": "Likewise in his words “Zayd is not anything except a thing”: if the excepted were carried on the wording of the excepted-from, “mā” would then have to be supposed in the same way so as to govern it;"},
    {"type": "matn",
     "ar": "(و«ما ولا» لا تقدران[[٦]]) لا حقيقة إذا لم يكن البدل إلا بتكرير العامل، ولا حكما إذا اكتفى بدخوله على المبدل",
     "en": "(and “mā” and “lā” are not supposed)—neither really, if the substitute is only by repetition of the governor, nor virtually, if one is content with its entering upon the substituted-for (mubdal)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لو مثل بالباء المزيدة لتأكيد غير الموجب نحو: ليس زيد بشيء، وهل زيد بشيء استيفاء للصور الأربع التي تعذر فيها حمل البدل على اللفظ لكان أولى.",
     "en": "Had he given an example with the bāʾ added to reinforce the non-affirmative, as in “Zayd is not anything (bi-shayʾ)” and “Is Zayd anything (bi-shayʾ)?”, so as to cover all four cases in which carrying the substitute on the wording is precluded, it would have been better."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لو لم يوصف به لصح أيضا لجواز أن يراد بالتنوين التحقير.",
     "en": "Had it not been qualified by it, it would also have been correct, since the tanwīn may be meant to express disparagement (taḥqīr)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما قيدها بها لأن «من» قد تكون زائدة في الموجب عند الأخفش إذا لم تكن استغراقية.",
     "en": "He restricted it by this only because, according to al-Akhfash, “min” may be redundant in an affirmative sentence when it is not all-inclusive."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: نفي مجرورها سواء باشرته أو لا، نحو: ما جاءني من رجل وامرأة.",
     "en": "That is, the negation of what it puts in the genitive, whether it is directly attached to it or not, as in “There did not come to me any man and woman.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ولو أبدل عمرا عن لفظ أحد لا يمكن نصب عمرو، بل لا بد من الرفع والتكرير؛ لأنه معرفة.",
     "en": "If “ʿAmr” were made a substitute for the wording of “aḥad,” the accusative of “ʿAmr” would not be possible; rather, the nominative and repetition [of “lā”] are necessary, because it is definite."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: لا تفرضان. وقوله: «عاملتين» تمييز؛ أو حال، أو مفعول ثان بتضمين معنى الجعل.",
     "en": "That is, they are not posited. His word “ʿāmilatayn” (as governing) is a specification (tamyīz), or a circumstantial (ḥāl), or a second object by the verb’s implying the sense of “making” (jaʿl)."},
]
