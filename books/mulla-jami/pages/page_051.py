# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 51 (printed ٥٠)."""

PAGE_NUMBER = 51
PRINTED_PAGE = "٥٠"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[ الاسم ]",
     "en": "[The Noun (al-Ism)]"},

    # ---------------- Main text (matn + sharḥ) ----------------
    {"type": "matn",
     "ar": "(الاسم: ما دل)[[١]] أي: كلمة دلت[[٢]] (على معنى) كائن (في نفسه)[[٣]] أي: في نفس ما دل[[٤]]، يعني: الكلمة.",
     "en": "(al-Ism [the noun]: that which indicates)[[١]] — that is, a word (kalima) that indicates[[٢]] (a meaning) subsisting (in itself)[[٣]], that is, in the very thing that indicates[[٤]], meaning the word (kalima)."},
    {"type": "matn",
     "ar": "فتذكير الضمير[[٥]] بناء على لفظ الموصول[[٦]].",
     "en": "The masculine gender of the pronoun[[٥]] is on account of the wording of the relative noun (al-mawṣūl)[[٦]]."},
    {"type": "matn",
     "ar": "قال المصنف في «الإيضاح شرح المفصل»: «الضمير في «ما دل على معنى في نفسه»[[٧]] يرجع إلى معنى، أي: ما دل على معنى باعتباره[[٨]] في نفسه[[٩]]، وبالنظر إليه[[١٠]]",
     "en": "The author (al-Muṣannif) said in al-Īḍāḥ, his commentary on al-Mufaṣṣal: “The pronoun in «that which indicates a meaning in itself»[[٧]] refers back to «meaning» — that is, that which indicates a meaning by consideration of it[[٨]] in itself[[٩]], and with regard to it[[١٠]]"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وإلا دخل في التعريف المركب والدوال الأربع، والقرينة على ذلك جعل الاسم من أقسام الكلمة.",
     "en": "Otherwise the definition would take in the compound (al-murakkab) and the four [types of] indicators (al-dawāll al-arbaʿ); the indication of this [restriction] is his making the ism one of the divisions of the word (kalima)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى أن كلمة «ما» كناية عن الكلمة لئلا يتناول هذا التعريف بعض المركبات والدوال الأربع.",
     "en": "A pointer that the word «mā» (that which) stands in for «the word» (al-kalima), lest this definition take in some of the compounds and the four indicators."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "جعله صفة لمعنى، سواء رجع ضميره إلى «ما» أو إلى المعنى، ولم يجعله ظرفا لغوا لـ«دل»، أو حالا عن ضميره،",
     "en": "He made it (kāʾin, “subsisting”) an adjective of «meaning» — whether its pronoun refers back to «mā» (that which) or to «the meaning» — and did not make it a non-essential adverbial (ẓarf laghw) governed by «indicates» (dalla), nor a circumstantial qualifier (ḥāl) of its pronoun,"},
    {"type": "pair",
     "ar": "حتى يكون معناها في الأول «ما دل بنفسه» أو «في نفس ذاته»، وعلى الثاني «كونه معتبرا في حد ذاته»؛",
     "en": "such that its sense, on the first [alternative], would be «that which indicates by itself» or «in its very essence», and on the second, «its being taken into account in its own right»;"},
    {"type": "pair",
     "ar": "لأن في جعل «في» بمعنى الباء خلاف المذهب المختار، ومجازا غير مشهور في التعريف، وأن الدلالة الوضعية غير ثابتة للفظ في حد ذاته، بل هي ثابتة له بالقياس إلى الوضع،",
     "en": "because construing «fī» (in) with the sense of the bāʾ (by) contravenes the preferred doctrine and is a non-established figurative usage within a definition; and because significative positing (al-dalāla al-waḍʿiyya) does not belong to the utterance in its own right, but rather belongs to it in relation to the act of positing (al-waḍʿ);"},
    {"type": "pair",
     "ar": "مع أن صحة تلك المعاني مبنية على قصور في دلالة الحرف، ولا قصور إلا في معناه لاحتياجه تصورا أو التفاتا إلى الغير. وذلك الاحتياج قبل الوضع السابق على الدلالة، وبالوضع لم يثبت حاجة أخرى بالذات.",
     "en": "moreover, the soundness of those interpretations rests upon a deficiency in the particle’s signification, and there is no deficiency except in its meaning, owing to its need — whether in conception (taṣawwur) or in attentive regard (iltifāt) — for another. Yet that dependence [belongs to what is] prior to the positing that precedes signification, and by the positing no further essential need is established."},
    {"type": "pair",
     "ar": "ولا يلزم من ذلك قصور في الدلالة، فإن كثيرا من المعاني الاسمية يتوقف على تصور الغير، وكثيرا منها يحتاج في تفهيمها إلى ضميمة، كتقدم المرجع في ضمير الغائب، والخطاب والتكلم في ضميري المخاطب والمتكلم، والإشارة في اسم الإشارة، وغير ذلك.",
     "en": "No deficiency in signification follows from this, for many nominal meanings depend upon conceiving another, and many of them require an adjunct for their being made understood — such as the antecedent’s precedence in the third-person pronoun, address and speaking in the second- and first-person pronouns, and pointing in the demonstrative noun, and so forth."},
    {"type": "pair",
     "ar": "والجملة: توقف فهم المسمى على شرط، لفظا كان أو غيره، لا يستلزم قصورا في الدلالة، كما لا يستلزم ذلك القصور توقفه على القائل والفاعل.",
     "en": "In sum: the dependence of understanding the named upon a condition — whether verbal or otherwise — does not entail a deficiency in signification, just as its dependence upon the speaker and the agent does not entail that deficiency."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا نفس الاسم، بأن يرجع الضمير إلى الاسم، وإلا يلزم الدور.",
     "en": "Not the noun itself — such that the pronoun would refer to the noun — for otherwise circularity (al-dawr) would follow."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: ضمير «في نفسه»، أو مطلق الضمير المذكور في «ما دل على معنى في نفسه» ليتناول الضمير المستتر في «دل» أيضا، فإن تذكيره أيضا بناء على لفظ الموصول.",
     "en": "That is: the pronoun of «fī nafsihi», or the pronoun mentioned in «that which indicates a meaning in itself» taken unrestrictedly, so as to include also the concealed pronoun in «dalla» — for its masculine gender too is on account of the wording of the relative noun."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ظاهر العبارة تدل على أن معنى الموصول يقتضي تأنيث الضمير باعتبار كونه كلمة، وتذكيره بملاحظة لفظه فقط.",
     "en": "The apparent wording indicates that the meaning of the relative noun requires the pronoun to be feminine (in view of its being a «kalima», a word), while its being masculine is only by regard to its wording."},
    {"type": "pair",
     "ar": "وفيه بحث، فإن لفظ كلمة «ما» عبارة عما يراد من لفظ الكلمة، لا عن لفظ الكلمة المشتمل على تاء التأنيث، وما يراد من لفظ الكلمة ليس فيه تأنيث كتأنيث «معنى» هنا مثلا،",
     "en": "But this is open to discussion, for the word «mā» stands for what is intended by the word «al-kalima», not for the wording «al-kalima» that contains the feminine tāʾ; and what is intended by the word «al-kalima» carries no feminine gender comparable to the feminine gender of «maʿnā» (meaning) here, for instance."},
    {"type": "pair",
     "ar": "فتأنيثه باعتبار اللفظ الدال على المعنى، وهو لفظ الكلمة، فإذا أخبر عنه بلفظ «ما» لم يكن فيه تأنيث لا في اللفظ ولا في المعنى، فتذكير الضمير الراجع إلى «ما» باعتبار اللفظ والمعنى.",
     "en": "So its feminine gender is by regard to the utterance signifying the meaning — namely the word «al-kalima»; and once it is predicated of by the word «mā», there is no feminine gender in it, neither in wording nor in meaning, so the masculine gender of the pronoun referring to «mā» is by regard to both wording and meaning."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: الضمير البارز، وإلا ففيه ضمير آخر أيضا لا يرجع إلى المعنى، بل إلى الموصول، وهو الضمير المستتر في «ما دل». ولو قال: الضمير «في نفسه» يرجع إلى المعنى لكان أخصر وأحفظ من المناقشة.",
     "en": "That is: the overt pronoun; otherwise it also contains another pronoun that does not refer to «the meaning» but to the relative noun — namely the concealed pronoun in «mā dalla» (that which indicates). Had he said: “the pronoun in «fī nafsihi» refers to the meaning,” it would have been more concise and better guarded against objection."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: المعنى.",
     "en": "That is: the meaning."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: في نفس المعنى.",
     "en": "That is: in the meaning itself."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: إلى المعنى.",
     "en": "That is: to the meaning."},
]
