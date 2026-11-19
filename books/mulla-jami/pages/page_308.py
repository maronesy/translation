# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 308 (printed ٣٠٧)."""

PAGE_NUMBER = 308
PRINTED_PAGE = "٣٠٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… فلا يكون» at the foot of PDF p. 307.
    {"type": "matn",
     "ar": "هيئة التركيب الإضافي موضوعة لمعلومية المضاف؟",
     "en": "…the form of the genitive composition coined for the annexed term’s being known?"},
    {"type": "matn",
     "ar": "قلنا: ذلك كما أن المعرف باللام في أصل الوضع لمعين، ثم قد يستعمل بلا إشارة إلى معين، كما في قوله:",
     "en": "We say: that is just as the noun made definite by the article (lām) is, in its original coinage, for a specific [referent], yet it is sometimes used without pointing to a specific [referent], as in the poet’s words:"},
    {"type": "verse",
     "ar": "ولقد أمر على اللئيم يسبني          فمضيت ثمت قلت: لا يعنيني",
     "en": "I pass by the base man as he reviles me; / I go on, and then I say: he does not mean me."},
    {"type": "matn",
     "ar": "وذلك على خلاف وضعه،",
     "en": "That is contrary to its coinage."},
    {"type": "matn",
     "ar": "وليس يجري هذا الحكم في نحو: «غير ومثل»[[١]]، فإن إضافتهما لا تفيد التعريف، وإن كانا مع المضاف إليه المعرفة لتوغلهما في الإبهام[[٢]]،",
     "en": "This rule does not apply to such words as “ghayr” (other than) and “mithl” (like), for their annexation does not convey definiteness, even when they are with a definite annexing term, because they are steeped in vagueness (ibhām);"},
    {"type": "matn",
     "ar": "إلا أن يكون للمضاف إليه ضد واحد يعرف بغيريته، كقولك: «عليك بالحركة غير السكون»،",
     "en": "unless the annexing term has a single contrary that is known by its being other than it, as when you say: “Hold to motion, other than rest”;"},
    {"type": "matn",
     "ar": "وكذلك إذا كان للمضاف إليه مثل اشتهر بمماثلته في شيء من الأشياء كالعلم والشجاعة، فقيل له: «جاء مثلك»، كان معرفة إذا قصد الذي يماثله في الشيء الفلاني.",
     "en": "likewise, if the annexing term has a like who is well known for resembling him in some respect, such as knowledge or courage, and it is said to him “your like came,” it is definite when what is meant is the one who resembles him in that particular respect."},
    {"type": "matn",
     "ar": "(و) تفيد الإضافة المعنوية (تخصيصا) أي: تخصيص المضاف (مع) المضاف إليه (النكرة) نحو: «غلام رجل»،",
     "en": "(And) the semantic genitive construction conveys (specification [takhṣīṣ]), that is, the specification of the annexed term, (with an indefinite) annexing term, as in “ghulām rajul” (a man’s slave);"},
    {"type": "matn",
     "ar": "فإن التخصيص تقليل الشركاء، ولا شك أن «الغلام» قبل إضافته إلى «رجل» كان مشتركا بين «غلام رجل، وغلام امرأة»،",
     "en": "for specification is the reduction of the sharers [in a name], and there is no doubt that “ghulām,” before its annexation to “rajul,” was shared between “a man’s slave” and “a woman’s slave”;"},
    {"type": "matn",
     "ar": "فلما أضيف إلى «رجل» خرج عنه «غلام امرأة»، وقلت الشركاء فيه.",
     "en": "when it was annexed to “rajul,” “a woman’s slave” was excluded from it, and the sharers in it became fewer."},
    {"type": "matn",
     "ar": "(وشرطها) أي: شرط الإضافة المعنوية: (تجريد المضاف) إذا كان معرفة (من التعريف)",
     "en": "(And its condition), that is, the condition of the semantic genitive construction, is (that the annexed term be stripped), if it is definite, (of definiteness):"},
    {"type": "matn",
     "ar": "فإن كان ذا لام حذف لامه، وإن كان علما نكر بأن يجعل[[٣]] واحدا من جملة من سمي بذلك الاسم،",
     "en": "if it bears the article (lām), its lām is dropped; and if it is a proper name (ʿalam), it is made indefinite by being made one of the whole group of those named by that name;"},
    {"type": "matn",
     "ar": "وإن لم يكن معرفة فلا حاجة إلى التجريد بل لا يمكن[[٤]] أو",
     "en": "and if it is not definite, there is no need for stripping; rather, it is not possible, or…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كنحو وشبه وغير ذلك.",
     "en": "Such as “naḥw” (the like of), “shibh” (resembling) and others."},
    {"type": "pair",
     "ar": "ولا يخفى عليك أنه ينبغي ألا يكون فرقا بين «غلام زيد» من غير إشارة إلى معين وبين مثل وغير في عدم إفادة الإضافة التعريف فيها،",
     "en": "It will not be hidden from you that there ought to be no difference between “ghulām Zayd” without pointing to a specific [individual] and “mithl” and “ghayr,” as regards the annexation not conveying definiteness in them;"},
    {"type": "pair",
     "ar": "مع أن الاستعمال فرق بينهما في تعريف وصف الأول دون الأخيرين.",
     "en": "yet usage distinguished between them, in that the qualifier of the first is definite, but not that of the last two."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأن مماثلة زيد في صفة لا تختص ذاتا. وكذا مغايرته، فإنه يشمل كل ما في الوجود إلا ذاته.",
     "en": "Because resembling Zayd in an attribute is not restricted to one entity. So too being other than him, for it includes everything in existence except himself."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كذا قال الشيخ الرضي. أراد به مثلا فإن تنكير العلم قد يكون بإرادة أشهر أوصافه،",
     "en": "So said Shaykh al-Raḍī. He meant it as an example, for making a proper name indefinite is sometimes done by intending the best known of its attributes;"},
    {"type": "pair",
     "ar": "أو أراد ما هو الغالب في التنكير، أو أراد أن تنكير العلم إذا أضيف لا يكون إلا كذلك.",
     "en": "or he meant what is predominant in making [a proper name] indefinite; or he meant that a proper name, when annexed, is made indefinite only in this way."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: وعندي أنه يجوز إضافة العلم مع بقاء تعريفه؛ إذ لا منع من اجتماع التعريفين إذا اختلفا كما ذكرنا في باب النداء.",
     "en": "Shaykh al-Raḍī said: In my view, a proper name may be annexed while keeping its definiteness, since nothing prevents two kinds of definiteness from combining when they differ, as we mentioned in the chapter on the vocative (al-nidāʾ)."},
    {"type": "pair",
     "ar": "وذلك إذا أضيف العلم إلى ما هو متصف به معنى نحو: زيد الشجاعة، فإنه يجوز وإن لم يكن في الدنيا إلا زيد واحد.",
     "en": "That is when the proper name is annexed to something with which it is qualified in meaning, as in “Zayd al-shajāʿa” (Zayd of courage); for this is permitted even if there is only one Zayd in the world."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأظهر أن المراد إيراده بلا تعريف.",
     "en": "The more evident [reading] is that what is meant is its being used without definiteness."},
]
