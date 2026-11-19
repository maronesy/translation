# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 299 (printed ٢٩٨)."""

PAGE_NUMBER = 299
PRINTED_PAGE = "٢٩٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows the verse «ولا أب وابنا مثل مروان وابنه …» at the foot of PDF p. 298 (new sentence).
    {"type": "matn",
     "ar": "وسائر التوابع لا نص عنهم فيها، لكن ينبغي أن يكون حكمها حكم توابع المنادى[[١]]، كذا ذكره الأندلسي.",
     "en": "As for the other dependents (tawābiʿ), there is no explicit statement from them about them; but their rule ought to be the rule of the dependents of the vocative (munādā). So al-Andalusī stated."},
    {"type": "matn",
     "ar": "(ومثل: «لا أبا له وغلامي له») أي: كل تركيب يكون فيه بعد اسم «لا» التي لنفي الجنس لام الإضافة،",
     "en": "(Such as “lā abā lahu” [he has no father] and “[lā] ghulāmay lahu” [he has no two slaves]), that is, every construction in which, after the noun of the “lā” that negates the genus, there comes the lām of annexation,"},
    {"type": "matn",
     "ar": "وأجري على ذلك الاسم أحكام الإضافة[[٢]] من إثبات الألف في نحو: «أب»، وحذف النون من نحو: «غلامين» (جائز)",
     "en": "and the rules of annexation are applied to that noun—keeping the alif in such as “ab” and dropping the nūn from such as “ghulāmayn”—(is permitted)."},
    {"type": "matn",
     "ar": "يعني: أن الأصل في مثل هذين التركيبين أن يقال: «لا أب له، ولا غلامين له»، فيكون اسم «لا» فيهما مبنيا على ما ينصب به، والجار مع مجروره خبرا لها،",
     "en": "He means: the default in the like of these two constructions is to say “lā aba lahu wa-lā ghulāmayni lahu,” the noun of “lā” in both being indeclinable on that by which it is put in the accusative, and the preposition with its object being its predicate;"},
    {"type": "matn",
     "ar": "وقد جاء على قلة مثل: «لا أبا له ولا غلامي له» بزيادة الألف في مثل: «أب»، وإسقاط النون في مثل: «غلامين» في حال الإضافة",
     "en": "but there has come, rarely, such as “lā abā lahu wa-lā ghulāmay lahu,” with the addition of the alif in such as “ab” and the dropping of the nūn in such as “ghulāmayn,” as in the state of annexation,"},
    {"type": "matn",
     "ar": "(تشبيها له) أي: لاسم «لا» في هذين التركيبين مع أنه ليس بمضاف (بالمضاف) وإجراء لأحكام المضاف عليه[[٣]] بإثبات الألف وحذف النون، فيكون معربا،",
     "en": "(by likening it), that is, the noun of “lā” in these two constructions, although it is not annexed, (to the annexed noun), and by applying the rules of the annexed noun to it—keeping the alif and dropping the nūn—so that it is declinable."},
    {"type": "matn",
     "ar": "وذلك التشبيه إنما هو (لمشاركته) أي: لمشاركة اسم «لا» حين يضاف[[٤]] بإظهار اللام بينه وبين ما يضاف إليه (له) أي: للمضاف (في أصل معناه)",
     "en": "That likening is only (because it shares), that is, because the noun of “lā,” when it is annexed with the lām expressed between it and what it is annexed to, shares (with it), that is, with the annexed noun, (in its basic meaning),"},
    {"type": "matn",
     "ar": "أي: معنى المضاف من حيث هو مضاف -يعني الإضافة- وهو الاختصاص[[٥]]،",
     "en": "that is, the meaning of the annexed noun qua annexed—he means annexation—which is specification (ikhtiṣāṣ)."},
    # REVIEW: print reads «أو المعنى إن مثل» where «أن مثل» is expected; transcribed as printed.
    {"type": "matn",
     "ar": "أو المعنى إن مثل: «لا أبا له، ولا غلامي له» جائز تشبيها له أي: لمثل هذين التركيبين حيث لا إضافة فيه بالمضاف،",
     "en": "Or the meaning is: such as “lā abā lahu wa-lā ghulāmay lahu” is permitted by likening it—that is, the like of these two constructions, in which there is no annexation—to the annexed,"},
    {"type": "matn",
     "ar": "أي: بتركيب يشتمل على الإضافة لمشاركته أي: لمشاركة مثل هذين التركيبين له أي: لما يشتمل على الإضافة في أصل معناه",
     "en": "that is, to a construction that contains annexation, because it shares—that is, because the like of these two constructions shares—with it, that is, with what contains annexation, in its basic meaning,"},
    {"type": "matn",
     "ar": "أي: معنى ما يشتمل على الإضافة، وهو الاختصاص",
     "en": "that is, the meaning of what contains annexation, which is specification;"},
    {"type": "matn",
     "ar": "إلا أن بين الاختصاصين تفاوتا، فإن الاختصاص المفهوم من التركيب الإضافي أتم مما يفهم من غيره.",
     "en": "except that there is a difference between the two specifications, for the specification understood from the annexation construction is more complete than what is understood from another."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: لأجل أن جواز مثل هذين التركيبين إنما هو بتشبيه غير المضاف",
     "en": "(Hence), that is, because the permissibility of the like of these two constructions is only through likening the non-annexed…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قيل: المفهوم من كلام الشيخ الرضي جواز البناء في البدل دون وجوبه.",
     "en": "It has been said: what is understood from the words of Shaykh al-Raḍī is that indeclinability in the substitute (badal) is permitted, not obligatory."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وذلك الاسم المثنى والجمع المذكر السالم والأسماء الستة إلا ذو، فإنه لا يقطع هذا عند المصنف.",
     "en": "That noun is the dual, the sound masculine plural and the six nouns except “dhū,” for according to the author this is not detached [from annexation]."},
    {"type": "pair",
     "ar": "وأما عند الشيخ الرضي فالأولان والأب والأخ.",
     "en": "According to Shaykh al-Raḍī, however, [it is] the first two, and “ab” (father) and “akh” (brother)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما زاد ذلك لئلا يتوهم أنه منصوب بالمشابهة بالمضاف؛",
     "en": "He added that only lest it be imagined that it is accusative through resemblance to the annexed noun;"},
    {"type": "pair",
     "ar": "إذ لو كان كذلك لنون لا أبا له كما ينون لا حسنا وجهه، ولم يحذف النون في لا غلامي.",
     "en": "for were it so, “lā abā lahu” would be given nunation, as “lā ḥasanan wajhuhu” (there is none handsome of face) is, and the nūn would not be dropped in “lā ghulāmay.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: print reads «سورة الإضافة» (with sīn); the sense requires «صورة الإضافة»; transcribed as printed.
    {"type": "pair",
     "ar": "يعني: أن صورة هذا التركيب سورة الإضافة باللام، وهو حال اعتبار الإضافة بوجود اللام مشارك للمضاف المقدر فيه اللام، هذا هو المعنى الأول.",
     "en": "He means: the form of this construction is the form of annexation with the lām; and, when annexation is considered through the presence of the lām, it shares with the annexed noun in which the lām is implied. This is the first meaning."},
    {"type": "pair",
     "ar": "وأما المعنى الثاني، فلا يعتبر فيه أنه في صورة المضاف، وأنه بهذا الاعتبار مشارك له.",
     "en": "As for the second meaning, it is not considered in it that it has the form of the annexed noun, nor that it shares with it in this respect."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "جعل الاختصاص أصل معنى الإضافة؛ لأن غيره من التعريف أو المعاني الأخرى قد يلحق به.",
     "en": "He made specification the basic meaning of annexation because other [meanings], such as definiteness or the other meanings, are sometimes attached to it."},
]
