# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 300 (printed ٢٩٩)."""

PAGE_NUMBER = 300
PRINTED_PAGE = "٢٩٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(ومن ثمة) أي: لأجل أن جواز مثل هذين التركيبين إنما هو بتشبيه غير المضاف» from the foot of PDF p. 299.
    {"type": "matn",
     "ar": "بالمضاف في معنى الاختصاص (لم يجز) تركيب («لا أبا فيها») أي: في الدار، لعدم الاختصاص،",
     "en": "…to the annexed noun in the meaning of specificity (ikhtiṣāṣ), (it is not permissible [to say]) the construction (“lā abā fīhā”), that is, “in the house” (there is no father in it), for lack of specificity;"},
    {"type": "matn",
     "ar": "فإن الاختصاص المفهوم من إضافة الأب إلى شيء إنما هو بأبوته له، وهذا الاختصاص غير ثابت للأب بالنسبة إلى الدار، فلا يصح إضافته إلى الدار،",
     "en": "for the specificity understood from annexing “father” to something consists only in his being its father, and this specificity does not hold for the father in relation to the house; so it is not sound to annex it to the house."},
    {"type": "matn",
     "ar": "فكيف يشبه تركيب «لا أبا فيها» بتركيب يضاف فيه الأب إلى الدار لمشاركته في أصل معناه.",
     "en": "How, then, could the construction “lā abā fīhā” be likened to a construction in which “father” is annexed to the house, on the ground that it shares in its basic meaning?"},
    {"type": "matn",
     "ar": "(وليس) أي: مثل هذين التركيبين (بمضاف) حقيقة (لفساد المعنى[[١]]) المراد المفاد بهما على تقدير الإضافة،",
     "en": "(And it is not), that is, such as these two constructions is not, (an annexed noun) in reality, (because of the corruption of the meaning) intended and conveyed by them, on the supposition of annexation (iḍāfa)."},
    {"type": "matn",
     "ar": "وهو نفي ثبوت جنس الأب أو الغلامين لمرجع الضمير المجرور بالاستقلال من غير احتياج إلى تقدير خبر،",
     "en": "That [meaning] is the negation that the genus of father, or of two slaves, holds for the referent of the genitive pronoun, independently, without need to suppose a predicate (khabar)."},
    {"type": "matn",
     "ar": "وهذا المعنى يفسد من وجهين على تقدير الإضافة:",
     "en": "This meaning is corrupted in two respects on the supposition of annexation:"},
    {"type": "matn",
     "ar": "أما أولا: فلأن معنى هذا التركيب على تقدير الإضافة: «لا أباه ولا غلاميه»، وهذا لا يتم إلا بتقدير خبر أي: «لا أباه موجود ولا غلاميه موجودان».",
     "en": "First, because the meaning of this construction on the supposition of annexation is “lā abāhu wa-lā ghulāmayhi” (not his father and not his two slaves), and this is not complete except by supposing a predicate, that is, “his father is not existent, and his two slaves are not existent.”"},
    {"type": "matn",
     "ar": "وأما ثانيا: فلأن المراد نفي ثبوت جنس الأب أو الغلامين له، لا نفي الوجود عن أبيه المعلوم أو غلاميه المعلومين",
     "en": "Second, because what is intended is the negation that the genus of father, or of two slaves, holds for him, not the negation of existence from his known father or his two known slaves,"},
    {"type": "matn",
     "ar": "(خلافا لسيبويه) والخليل وجمهور النحاة،",
     "en": "(contrary to Sībawayh), al-Khalīl and the majority of the grammarians."},
    {"type": "matn",
     "ar": "وإنما خص سيبويه بهذا الخلاف؛ لأنه العمدة فيما بينهم[[٢]]، أو لأن المقصود بيان الخلاف لا تعيين المخالفين[[٣]]،",
     "en": "He singled out Sībawayh for this disagreement only because he is the chief authority among them, or because the aim is to state the disagreement, not to identify those who disagree."},
    {"type": "matn",
     "ar": "فمذهب سيبويه والخليل وجمهور النحاة أن مثل هذا التركيب مضاف حقيقة باعتبار المعنى، وإقحام اللام بين المضاف والمضاف إليه تأكيد للام المقدرة،",
     "en": "The doctrine of Sībawayh, al-Khalīl and the majority of the grammarians is that such a construction is really annexed with respect to meaning, and that the insertion of the lām between the annexed noun and the noun to which it is annexed is a reinforcement of the implied lām;"},
    {"type": "matn",
     "ar": "وحكم المصنف بفساده لما عرفت.",
     "en": "and the author judged it corrupt for the reason you have learned."},
    {"type": "matn",
     "ar": "(ويحذف) اسم «لا» حذفا كثيرا (في مثل: «لا عليك») أي: «لا بأس عليك»،",
     "en": "(And it is elided), that is, the noun of “lā” is frequently elided, (in such as “lā ʿalayka”), that is, “lā baʾsa ʿalayka” (no harm upon you);"},
    {"type": "matn",
     "ar": "ولا يحذف إلا مع وجود الخبر[[٤]]، لئلا يكون إجحافا.",
     "en": "and it is elided only when the predicate is present, so that it does not amount to excessive curtailment (ijḥāf)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال المصنف: ولأنه لو كان مضافا لزم الرفع والتكرير.",
     "en": "The author said: and because, were it annexed, the nominative and repetition would be required."},
    {"type": "pair",
     "ar": "وفيه أن الصورة غيرت لئلا يلزم ذلك.",
     "en": "Against this [it is said] that the form was altered so that this would not be required."},
    # REVIEW: print reads «يتسر»; probably a misprint for «يتيسر»; transcribed as printed.
    {"type": "pair",
     "ar": "قالوا: الحامل على هذا التغيير قصد النصب من غير تكرير لا تخفيفا. وذا لا يتسر مع المعرفة.",
     "en": "They said: what prompted this alteration was the aim of [having] the accusative without repetition, not lightening; and this is not feasible with a definite noun."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه بحث؛ لأنه حكم المحقق الشريف قدس سره في شرح الكشاف أن الخليل أعلى كعبا منه.",
     "en": "This is open to question, for the verifying scholar al-Sharīf [al-Jurjānī], may his secret be sanctified, judged in his commentary on al-Kashshāf that al-Khalīl was of higher standing than he."},
    {"type": "pair",
     "ar": "وقال صاحب إعراب الفاتحة: لم يسبق الخليل فيما بين علماء النحو مثل له، ولم يخلف فيما بينهم مثلا له.",
     "en": "And the author of Iʿrāb al-Fātiḥa said: among the scholars of grammar no equal to al-Khalīl preceded him, and he left no equal to himself among them."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا يخفى بعده من العبارة.",
     "en": "Its remoteness from the wording is evident."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كما لا يحذف الخبر إلا مع وجود الاسم بعين هذه العلة.",
     "en": "Just as the predicate is elided only when the noun is present, for this very reason."},
    {"type": "pair",
     "ar": "ويمكن أن يراد بقوله: مثل «لا عليك» تركيب ذكر فيه الخبر.",
     "en": "It is possible that by his words “such as ‘lā ʿalayka’” is meant a construction in which the predicate is mentioned."},
]
