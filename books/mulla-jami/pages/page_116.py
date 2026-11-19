# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 116 (printed ١١٥)."""

PAGE_NUMBER = 116
PRINTED_PAGE = "١١٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The main commentary (matn) ----------------
    {"type": "matn",
     "ar": "في منع دخول تاء التأنيث عليهما[[١]].",
     "en": "in [their both] preventing the tāʾ of femininity from entering upon them."},
    {"type": "matn",
     "ar": "وللنحاة خلاف في أن سببيتهما لمنع الصرف: إما كونهما مزيدتين، وفرعيتهما للمزيد عليه[[٢]].",
     "en": "The grammarians differ as to the ground of their being a cause for preventing full inflection: it is either their being augmentative and their subordinacy (farʿiyya) to that upon which they are added,"},
    {"type": "matn",
     "ar": "وإما مشابهتهما لألفي التأنيث[[٣]]. والراجح هو القول الثاني[[٤]].",
     "en": "or it is their resemblance to the two alifs of the feminine. And the preponderant view is the second position."},
    {"type": "matn",
     "ar": "ثم إنهما (إن كانا في اسم) يعنى به: ما يقابل الصفة[[٥]]، فإن الاسم المقابل للفعل والحرف: إما ألا يدل[[٦]] على ذات ما لوحظ معها صفة من الصفات كـ«رجل وفرس»، أو يدل كـ«أحمر، وضارب، ومضروب».",
     "en": "Then [he says] that these two, (if the two occur in a noun) — by which is meant that which is opposed to the qualifier (ṣifa); for the noun opposed to the verb and the particle either does not signify an essence together with which some attribute is considered — as in “man” and “horse” — or it does so signify, as in “red,” “striker,” and “struck.”"},
    {"type": "matn",
     "ar": "فالأول: يسمى اسما.",
     "en": "The first is called a noun (ism)."},
    {"type": "matn",
     "ar": "والثاني: صفة.",
     "en": "The second is a qualifier (ṣifa)."},
    {"type": "matn",
     "ar": "فالمراد بالاسم المذكور ههنا هو هذا المعنى، لا الاسم الشامل[[٧]] للاسم والصفة.",
     "en": "So what is intended by “the noun” mentioned here is this [narrower] sense, not the noun that encompasses both the noun and the qualifier."},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ضمير التثنية في «عليهما» يحتمل ثلاث احتمالات: الأول: أن يرجع إلى الألف والنون المزيدتين، والثاني: أن يرجع إلى ألفي التأنيث، والثالث: أن يرجع إلى مجموع المشبه والمشبه به،",
     "en": "The dual pronoun in “upon them” (ʿalayhimā) admits three possibilities: the first, that it refers to the augmentative alif and nūn; the second, that it refers to the two alifs of the feminine; the third, that it refers to the totality of the likened thing (mushabbah) and that to which it is likened (mushabbah bihi);"},
    {"type": "pair",
     "ar": "وعلى التقادير المراد اشتراك المشبه والمشبه به في هذه الصفة كما لا يخفى.",
     "en": "and on all these estimations, what is intended is that the likened thing and that to which it is likened share in this attribute, as is not hidden."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يظهر على هذا التقدير وجه اشتراطهم انتفاء التاء إلا أن يقال: وجهه أن المجرد عن التاء أصل لما زيد عليه التاء، والأصالة تنافي الفرعية التي تؤثران بسببها.",
     "en": "On this estimation the reason for their stipulating the absence of the tāʾ does not appear, unless it be said: its reason is that what is stripped of the tāʾ is the base (aṣl) for that to which the tāʾ is added, and being a base is incompatible with the subordinacy by reason of which the two [letters] exert their effect."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: في منع دخول تاء التأنيث.",
     "en": "That is: in preventing the tāʾ of femininity from entering."},
    {"type": "pair",
     "ar": "إن قلت: لا بد في السبب من فرعية ولا فرعية على هذا المذهب؟",
     "en": "If you say: a cause must possess subordinacy, yet there is no subordinacy on this position?"},
    {"type": "pair",
     "ar": "قلنا: السبب إما المشابهة أو المشابه، فإن كان الأولى فهي فرع للطرفين وهو ظاهر، وإن كان الثاني فهو فرع لما زيد عليه، لكنه سبب غير أصلي لتوقفه على المشابهة مع أن المشبه من عداد المشبه به، فلا حاجة فيه إلى إثبات فرعية مغايرة لفرعية المشبه به.",
     "en": "We reply: the cause is either the likening (mushābaha) or the likened [thing]. If it is the former, then it is subordinate to both sides, which is evident; and if it is the latter, then it is subordinate to that upon which it is added, but it is a non-original cause because it depends on the likening — given that the likened thing is counted among that to which it is likened — so there is no need in it to establish a subordinacy distinct from the subordinacy of that to which it is likened."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأن اشتراط انتفاء فعلانة على القول الأول غير ظاهر. وإن قيل: إنه ليتحقق فرعيتهما من غير شائبة أصالة؛",
     "en": "Because the stipulation of the absence of a faʿlāna [feminine form] is not evident on the first position. And even if it be said: it is so that their subordinacy may be realized without any admixture of originality;"},
    {"type": "pair",
     "ar": "إذ لو دخل التاء لكانا أصليتين للتاء الزائدة عليهما؛ لأنه لو ضعفت الفرعية بزيادة شيء عليه لضعفت بزيادة في التثنية.",
     "en": "for had the tāʾ entered, the two would be original relative to the tāʾ added upon them — since, were subordinacy weakened by something being added to it, it would [also] be weakened by the addition [that occurs] in the dual."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: لا ما يقابل الفعل والحرف. وأما من قال: ولا الاسم المقابل للكنية، والمقابل للمهمل، والمقابل للظرف اللازم الظرفية أتى بما لا يعنيه؛",
     "en": "That is: not that which is opposed to the verb and the particle. As for one who said, “nor the noun opposed to the agnomen (kunya), the one opposed to the meaningless [sound], and the one opposed to the adverb permanently fixed in adverbiality,” he has produced what is of no concern to him;"},
    {"type": "pair",
     "ar": "إذ لا يذهب السامع في هذا المقام إلى غير المقابل للفعل والحرف، حتى يحتاج الشارح إلى نفيه.",
     "en": "for in this context the hearer’s mind does not go to anything other than that which is opposed to the verb and the particle, such that the commentator would need to negate it."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قدم المفهوم العدمي على الوجودي مع شرف الوجودي، ومع أن الأعدام تعرف بملكاتها؛",
     "en": "He gave precedence to the privative concept over the positive concept, despite the nobility of the positive, and despite the fact that privations are known through their [correlative] possessions (malakāt);"},
    {"type": "pair",
     "ar": "لأن المفهوم العدمي مفهوم الاسم، والمفهوم الوجودي مفهوم الصفة، والاسم مقدم على الصفة في نفسه، وفي كلام المصنف أيضا.",
     "en": "because the privative concept is the concept of the noun, and the positive concept is the concept of the qualifier, and the noun takes precedence over the qualifier in itself, and in the author’s wording as well."},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "ولا الاسم المقابل للقب والكنية، والمقابل للمهمل، والمقابل للظرف اللازم الظرفية.",
     "en": "Nor the noun opposed to the epithet (laqab) and the agnomen (kunya), nor the one opposed to the meaningless [sound], nor the one opposed to the adverb permanently fixed in adverbiality."},
]
