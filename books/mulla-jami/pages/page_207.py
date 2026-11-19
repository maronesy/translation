# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 207 (printed ٢٠٦)."""

PAGE_NUMBER = 207
PRINTED_PAGE = "٢٠٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # continues from p.206: «(والمعطوف) بحرف (الممتنع دخول»
    {"type": "matn",
     "ar": "«يا» عليه[[١]]) يعني المعرف باللام،",
     "en": "…“yā” on it), meaning: the one made definite by the lām,"},
    {"type": "matn",
     "ar": "بخلاف البدل والمعطوف الغير الممتنع دخول «يا» عليه، فإن حكمهما غير حكمها كما سيجيء.",
     "en": "as opposed to the substitute (badal) and the coordinated noun on which the entry of “yā” is not barred; for their rule differs from the rule of these, as will come."},
    {"type": "matn",
     "ar": "(ترفع[[٢]] حملا على لفظه) الظاهر أو المقدر[[٣]]؛",
     "en": "(They take the nominative, by construction on its wording), whether apparent or implied;"},
    {"type": "matn",
     "ar": "لأن بناء المنادى عرضي، فيشبه المعرب، فيجوز أن يكون تابعه تابعا للفظه.",
     "en": "because the indeclinability (bināʾ) of the vocative (munādā) is accidental, so it resembles the declinable, and its appositive (tābiʿ) may therefore follow its wording."},
    {"type": "matn",
     "ar": "(وتنصب حملا على محله)؛ لأن حق توابع المبني أن يكون تابعا لمحله،",
     "en": "(And they take the accusative, by construction on its position); because what is due to the appositives of an indeclinable noun is that they follow its position,"},
    {"type": "matn",
     "ar": "وهو ههنا منصوب المحل بالمفعولية",
     "en": "and here it is accusative in position as an object,"},
    {"type": "matn",
     "ar": "نحو: «يا تميم أجمعون وأجمعين» في التأكيد، و«يا زيد العاقل والعاقل» في الصفة،",
     "en": "as in: “O Tamīm, all of you” (yā Tamīmu ajmaʿūna / ajmaʿīna) for the corroborative (taʾkīd), and “O Zayd, the intelligent” (yā Zaydu al-ʿāqilu / al-ʿāqila) for the qualifier (ṣifa);"},
    {"type": "matn",
     "ar": "واقتصر على مثالها[[٤]]؛ لأنها أكثر وأشهر استعمالا،",
     "en": "he confined himself to its example because it is the more frequent and better known in usage;"},
    {"type": "matn",
     "ar": "و«يا غلام بشر وبشرا» في عطف البيان، و«يا زيد والحارث» في المعطوف بحرف الممتنع دخول «يا» عليه.",
     "en": "and “O boy, Bishr” (yā ghulāmu Bishrun / Bishran) for the explicative apposition (ʿaṭf al-bayān), and “O Zayd and al-Ḥārith” (yā Zaydu wa-l-Ḥārithu / wa-l-Ḥāritha) for the noun coordinated by a particle on which the entry of “yā” is barred."},
    {"type": "matn",
     "ar": "(والخليل) ابن أحمد -وهو أستاذ سيبويه[[٥]]- (في المعطوف) بحرف الممتنع دخول «يا» عليه[[٦]] (يختار الرفع) مع تجويزه النصب[[٧]]؛",
     "en": "(And al-Khalīl) ibn Aḥmad—he is the teacher of Sībawayh—(in the coordinated noun) by a particle on which the entry of “yā” is barred (prefers the nominative), while allowing the accusative;"},
    {"type": "matn",
     "ar": "لأن المعطوف بحرف[[٨]] في",
     "en": "because the noun coordinated by a particle is in…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لم يقل: والمعطوف المعرف باللام مع أنه أخصر ليشعر إلى مانع الاستقلال، وهو امتناع دخول \"يا\" عليه،",
     "en": "He did not say “and the coordinated noun made definite by the lām,” although that is shorter, in order to point to what prevents independence, namely that “yā” is barred from entering it,"},
    {"type": "pair",
     "ar": "وليخرج نحو: يا محمد والله لتعين الرفع.",
     "en": "and in order to exclude such as “O Muḥammad and Allah” (yā Muḥammadu wa-llāhu), because the nominative is fixed there."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولا تبنى الصفة كما في \"لا رجل ظريف\"؛ لأن النفي متوجه إلى الصفة دون النداء،",
     "en": "The qualifier is not made indeclinable, as it is in “lā rajula ẓarīfa” (no witty man), because the negation is directed to the qualifier, whereas vocation is not;"},
    {"type": "pair",
     "ar": "والرافع هو حرف النداء لشبهها بالرافع في كون أثر كل عارضا مطردا،",
     "en": "and what puts it in the nominative is the vocative particle, because of its resemblance to a nominative governor in that the effect of each is accidental and regular;"},
    {"type": "pair",
     "ar": "ولم يظهر أثر هذا الشبه في المنادى لمكان البناء.",
     "en": "the effect of this resemblance does not appear in the vocative itself because of its indeclinability."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "مثل: يا فتى ويا هؤلاء، فإن ضمتهما تقديرية مفروضة، كما ذهب إليه الشيخ الرضي.",
     "en": "Such as “yā fatā” (O youth) and “yā hāʾulāʾi” (O these), for their ḍamma is implied and supposed, as Shaykh al-Raḍī held."},
    {"type": "pair",
     "ar": "والأظهر أن يقال: أن لهؤلاء ضما محليا؛ لأن مفردا معرفة معربا لو وقع موقعه لضم",
     "en": "The more evident view is to say that “hāʾulāʾi” has a ḍamma by position (maḥallī), because a definite, singular, declinable noun in its place would take the ḍamma,"},
    {"type": "pair",
     "ar": "كما أن له نصبا محليا؛ لأن مضافا لو وقع موقعه لكان منصوبا.",
     "en": "just as it has an accusative by position, because an annexed noun in its place would be accusative."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأنه أول ما يمكن أن يمثل فيه بالمعرف باللام المنافي لحرف النداء،",
     "en": "Because it is the first in which one can give an example with a noun made definite by the lām, which is incompatible with the vocative particle;"},
    {"type": "pair",
     "ar": "وهو أولى بالتمثيل ليعلم أنه ثبت فيه أثر حرف النداء مع منافاته له.",
     "en": "and it is more fitting for illustration, so that it be known that the effect of the vocative particle is established in it despite its incompatibility with it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وهو الذي قال صاحب إعراب الفاتحة في شأنه: لم يتقدمه مثله، ولم يخلف مثله.",
     "en": "He is the one of whom the author of Iʿrāb al-Fātiḥa said: none like him preceded him, and none like him came after him."},
    {"type": "pair",
     "ar": "وقال المحقق الشريف في حاشية الكشاف: وهو أعلى كعبا من سيبويه.",
     "en": "And the verifier al-Sharīf [al-Jurjānī] said in his gloss on al-Kashshāf: he is of higher standing than Sībawayh."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني: أن اللام للعهد والجار والمجرور متعلق بقوله: يختار.",
     "en": "He means: the lām [of al-maʿṭūf] is for prior reference (ʿahd), and the preposition with its object is attached to his word “yakhtāru” (prefers)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأن المراد بالاختيار الحكم بالأولوية.",
     "en": "Because what is meant by “preference” is the judgement that [one option] is the more fitting."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "نظر أبو عمرو إلى جانب اللفظ، ونظر الخليل إلى جانب المعنى واستقلاله، فجعله مرفوعا تنبيها على الاستقلال.",
     "en": "Abū ʿAmr looked to the side of the wording, while al-Khalīl looked to the side of the meaning and its independence, and so made it nominative to draw attention to its independence."},
    {"type": "pair",
     "ar": "إن قلت: ينبغي أن يختار الرفع إذا كان المتبوع غير المضموم تعين هذا الوجه؟",
     "en": "If you say: the nominative ought to be preferred [also] when the antecedent is not in the ḍamma—this alternative being then fixed?"},
    {"type": "pair",
     "ar": "أجيب عنه: بأنه أراد التنبيه على الاستقلال مع رعاية الاتباع اللفظي، ولا يتصور ذلك إلا إذا كان المتبوع مضموما.",
     "en": "It has been answered: he intended to draw attention to independence while observing concord with the wording (al-itbāʿ al-lafẓī), and that is conceivable only when the antecedent is in the ḍamma."},
]
