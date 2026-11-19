# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 571 (printed ٥٧٠)."""

PAGE_NUMBER = 571
PRINTED_PAGE = "٥٧٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 570 ends with a complete sentence on ḥattā; this page opens a new lemma.
    {"type": "matn",
     "ar": "(ومعطوفها) أي: المعطوف بـ«حتى» بحسب ما اقتضاه وضعها[[١]] (جزء) قوي أو ضعيف من حيث إنه قوي[[٢]] أو ضعيف.",
     "en": "(And what is coordinated by it), that is, what is coordinated by “ḥattā”, according to what its coinage (waḍʿ) requires, (is a part), strong or weak, inasmuch as it is strong or weak,"},
    {"type": "matn",
     "ar": "(من متبوعه) أي: متبوع معطوفها (ليفيد) أي: العطف بها (قوة) في المعطوف (أو ضعفا فيه) أي: ليدل عليهما[[٣]]",
     "en": "(of what it follows), that is, of what its coordinated term follows, (so that it conveys), that is, coordination by it [conveys], (strength) in the coordinated term (or weakness in it), that is, so that it indicates these two,"},
    {"type": "matn",
     "ar": "حتى يتميز الجزء بالقوة والضعف عن الكل، فصار كأنه غيره، فصلح لأن تجعل غاية وانتهاء للفعل المتعلق بالكل،",
     "en": "so that the part is distinguished from the whole by strength and weakness and becomes as though it were other than it; it is then fit to be made the limit (ghāya) and termination of the action that attaches to the whole,"},
    {"type": "matn",
     "ar": "ودل انتهاء الفعل[[٤]] إليه على مشموله جميع أجزاء الكل، نحو: «مات الناس حتى الأنبياء»، و«قدم الحاج حتى المشاة».",
     "en": "and the action’s terminating at it indicates that it covers all the parts of the whole, as in “the people died, even the prophets” and “the pilgrims arrived, even those on foot”."},
    {"type": "matn",
     "ar": "والفرق بين «ثم» و«حتى» بعد اشتراكهما في الترتيب مع المهلة، من وجهين[[٥]]:",
     "en": "The difference between “thumma” and “ḥattā”, after their sharing in order with delay (muhla), is in two respects:"},
    {"type": "matn",
     "ar": "أحدهما: اشتراط كون المعطوف بـ«حتى» جزءا من متبوعه، ولا يشترط ذلك في «ثم».",
     "en": "the first is the requirement that what is coordinated by “ḥattā” be a part of what it follows, while this is not required for “thumma”."},
    {"type": "matn",
     "ar": "وثانيهما: أن المهلة المعتبرة في «ثم» إنما هي بحسب الخارج نحو: «جاءني زيد ثم عمرو» وفي «حتى» بحسب الذهن،",
     "en": "The second is that the delay taken into account in “thumma” is only according to external reality, as in “Zayd came to me, then ʿAmr”, whereas in “ḥattā” it is according to the mind;"},
    {"type": "matn",
     "ar": "فإن المناسب بحسب الذهن أن يتعلق الموت أولا بغير الأنبياء، ويتعلق بعد التعلق بهم بالأنبياء؛ إن كان موت الأنبياء بحسب الخارج في أثناء سائر الناس،",
     "en": "for what is fitting according to the mind is that death attach first to those other than the prophets, and, after attaching to them, attach to the prophets, even if the death of the prophets, according to external reality, came in the midst of the rest of the people."},
    {"type": "matn",
     "ar": "وهكذا المناسب في الذهن تقدم قدوم ركبان الحاج على رجالتهم[[٦]]، وإن كان في بعض الأوقات على عكس ذلك، ومع هذا يصح أن يقال: «قدم الحاج حتى المشاة».",
     "en": "Likewise, what is fitting in the mind is that the arrival of the mounted pilgrims precede that of those on foot, even if at some times it is the reverse; and despite this it is correct to say “the pilgrims arrived, even those on foot”."},
    {"type": "matn",
     "ar": "واعلم أن الانتهاء بالجزء الأقوى أو الأضعف، كما يفيد عموم الفعل جميع أجزاء الشيء كذلك الانتهاء بالملاقي للجزء الأخير يفيد ذلك العموم،",
     "en": "Know that, just as termination at the strongest or weakest part conveys that the action covers all the parts of the thing, so termination at what adjoins the last part conveys that same generality,"},
    {"type": "matn",
     "ar": "كقولك: «نمت البارحة حتى الصباح»، فإنه يفيد شمول النوم لجميع أجزاء الليلة،",
     "en": "as in your saying “I slept last night until the morning”, for it conveys that the sleep covered all the parts of the night;"},
    {"type": "matn",
     "ar": "ولذلك استعملت «حتى» الجارة في المعنيين جميعا، إلا أنه لم يأت في العاطفة ما يلاقي الجزء الأخير، فإن",
     "en": "for this reason the genitive-governing “ḥattā” is used in both senses together, except that in the coordinating [ḥattā] what adjoins the last part does not occur; for…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإنها موضوعة للتدريج الذهني.",
     "en": "For it is coined for gradation in the mind."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيد بذلك ليترتب عليه قوله: ليفيد قوة أو ضعفا،",
     "en": "He qualified it thus so that his words “so that it conveys strength or weakness” follow from it,"},
    {"type": "pair",
     "ar": "فإن ليفيد متعلق بمفهوم الكلام، فكأنه قال: يعطف بها جزء من المعطوف ليفيد إلى آخره.",
     "en": "for “li-yufīda” is attached to the sense of the statement, as though he had said: “a part of the coordinated is coordinated by it, so that it conveys…” to the end."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: printed «ليس المراد بالإفادة في الخارج في الذهن»; a word such as «بل» seems missing before «في الذهن»; transcribed as printed.
    {"type": "pair",
     "ar": "أي: ليس المراد بالإفادة في الخارج في الذهن.",
     "en": "That is, what is meant by “conveying” is not in external reality, [but] in the mind."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: printed «قدم الحجاج»; the matn has «قدم الحاج»; transcribed as printed.
    {"type": "pair",
     "ar": "فيصير معنى الكلام نصا في الشمول، بخلاف ما إذا لم يذكر حتى نحو: قدم الحجاج.",
     "en": "So the sense of the statement becomes explicit (naṣṣ) in comprehensiveness, unlike when “ḥattā” is not mentioned, as in “the pilgrims arrived”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بل من ثلاثة أوجه، ثالثها: ما تقدم من أن المهملة في «حتى» أقل.",
     "en": "Rather, in three respects, the third being what preceded: that the delay in “ḥattā” is less."},
    # REVIEW: printed «المهملة» for «المهلة»; transcribed as printed.

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الراجل خلاف الفارس، والجمع رجل نحو: صاحب وصحب ورجال ورجالة، كذا في الصحاح،",
     "en": "Al-rājil (one on foot) is the opposite of al-fāris (horseman); the plural is rajl, like ṣāḥib and ṣaḥb, and rijāl and rajjāla; so in al-Ṣiḥāḥ."},
    {"type": "pair",
     "ar": "والمشاة جمع ماش.",
     "en": "Al-mushāt is the plural of māshin (one walking)."},
]
