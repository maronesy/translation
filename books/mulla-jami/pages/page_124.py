# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 124 (printed ١٢٣)."""

PAGE_NUMBER = 124
PRINTED_PAGE = "١٢٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "(إذا نكر اعتبارا[[١]] للصفة الأصلية) أي: إنما خالف سيبويه الأخفش، لأجل اعتباره الوصفية الأصلية[[٢]] (بعد التنكير)، فإنه لما زالت العلمية بالتنكير لم يبق مانع من اعتبار الوصفية، فاعتبرها وجعله غير منصرف للصفة الأصلية، وسبب آخر، كوزن الفعل[[٣]] والألف والنون المزيدتين.",
     "en": "(when it is made indefinite, by reckoning the original descriptiveness): that is, Sībawayh differed from al-Akhfash only on account of his reckoning the original descriptiveness (after being made indefinite); for when proper-nounhood departed through indefiniteness, no impediment to reckoning descriptiveness remained, so he reckoned it and made [the word] non-inflecting on account of the original descriptiveness and another cause — such as the pattern of the verb, or the added alif and nūn."},
    {"type": "matn",
     "ar": "فإن قلت: كما أنه لا مانع من اعتبار الوصفية الأصلية لا باعث على اعتبارها أيضا، فلم اعتبرها؟ وذهب إلى ما هو خلاف الأصل[[٤]] فيه، أعني: منع الصرف؟",
     "en": "If you say: just as there is no impediment to reckoning the original descriptiveness, so too there is no motive for reckoning it; so why did he reckon it, and adopt in it what is contrary to the base — I mean, the prevention of full inflection?"},
    {"type": "matn",
     "ar": "قيل: الباعث على اعتبارها امتناع «أسود» و«أرقم» مع زوال الوصفية عنهما[[٥]] حينئذ، وفيه بحث[[٦]]؛ لأن الوصفية لم تزل عنهما بالكلية، بل بقي فيهما شائبة من الوصفية؛ لأن «الأسود» اسم للحية السوداء، و«الأرقم» للحية التي فيها سواد وبياض، وفيهما شمة من الوصفية، فلا يلزم من اعتبار الوصفية فيهما اعتبارها في «أحمر» بعد التنكير؛ لأنها قد زالت عنه بالكلية.",
     "en": "It is said: the motive for reckoning it is the non-inflection of “aswad” and “arqam,” despite descriptiveness having departed from them in that case. But there is a discussion in this, because descriptiveness has not departed from them entirely; rather, a tinge of descriptiveness remains in them — for “al-aswad” is a name for the black snake, and “al-arqam” for the snake that has blackness and whiteness in it, so in them there is a trace of descriptiveness. Hence, from reckoning descriptiveness in them, it does not follow that it be reckoned in “aḥmar” after being made indefinite, because it has departed from it entirely."},
    {"type": "matn",
     "ar": "وأما الأخفش[[٧]] فذهب إلى أنه منصرف، فإن الوصفية قد زالت بالعلمية، والعلمية بالتنكير، والزائل لا يعتبر من غير ضرورة، فلم يبق فيه إلا سبب واحد، وهو وزن الفعل أو الألف والنون، وهذا القول أظهر[[٨]].",
     "en": "As for al-Akhfash, he held that it is fully inflected; for descriptiveness departed through proper-nounhood, and proper-nounhood through being made indefinite, and what has departed is not reckoned without necessity. So there remained in it but a single cause — namely, the pattern of the verb, or the alif and nūn. And this doctrine is the more evident."},
    {"type": "matn",
     "ar": "ولما اعتبر سيبويه الوصف الأصلي بعد التنكير، وإن كان زائلا لزمه أن يعتبره في حال العلمية أيضا، فيمتنع نحو: «حاتم» من الصرف للوصف الأصلي والعلمية.",
     "en": "And since Sībawayh reckoned the original descriptiveness after being made indefinite, even though it has departed, it became binding upon him to reckon it also in the state of proper-nounhood; so the like of “Ḥātim” is barred from full inflection on account of the original descriptiveness and proper-nounhood."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يجوز أن يكون مصدرا لـ«خالف»؛ لأن ذلك الاعتبار نوع مخالفة.",
     "en": "It may be a verbal noun of “khālafa” (he differed), because that reckoning is a kind of differing."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بمعنى أن المعدوم يجعله كالثابت.",
     "en": "In the sense that he treats what is non-existent as though it were established."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: في مثل أحمر، والألف والنون في نحو: سكران.",
     "en": "That is: [the pattern of the verb] in the like of “aḥmar,” and the alif and nūn in the like of “sakrān.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: باعتبار هذا المحذور. وهو الذهاب إلى خلاف الأصل، وهو منع الصرف.",
     "en": "He means: by reckoning this objectionable consequence — namely, adopting what is contrary to the base, which is the prevention of full inflection."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: أن أسود وأرقم حال غلبة الإسمية زائل الوصفية، مع أنهم اعتبروها وجعلوا أسود وأرقم غير منصرف للوصفية ووزن الفعل، فاعتبارها بعد العلمية أولى.",
     "en": "He means: that “aswad” and “arqam,” in the state where nounhood predominates, have lost their descriptiveness; yet they [the grammarians] reckoned it and made “aswad” and “arqam” non-inflecting on account of descriptiveness and the pattern of the verb — so reckoning it after proper-nounhood is all the more fitting."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إن قيل: جاز اعتبار شمة من الوصفية في العلم كما إذا سميت بـ«أحمر» من فيه حمرة؟",
     "en": "If it be said: might a trace of descriptiveness be reckoned in the proper name, as when one names “Aḥmar” someone who has redness in him?"},
    {"type": "pair",
     "ar": "أجيب بأن المقصود الأهم في وضع الأعلام المنقولة غير ما وضع له لغة. ولذلك تراها مجردة عن المعنى الأصلي كـ«زيد».",
     "en": "The reply is that the more important aim in coining transferred proper names is other than that for which [the word] was coined lexically; and for this reason you see them stripped of the original meaning, like “Zayd.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال الرضي: قال الأخفش في كتاب الأوسط: إن خلافه في نحو: أحمر إنما هو في مقتضى القياس. وأما السماع فهو على منع الصرف.",
     "en": "Al-Raḍī said: al-Akhfash said in the book al-Awsaṭ: his disagreement regarding the like of “aḥmar” is only concerning what analogy requires; but as for transmitted usage (samāʿ), it accords with the prevention of full inflection."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وقد سبق ما دل على كونه أظهر. ومن موجباته أن العلمية الأصلية تمتنع عن اعتبارها؛ لأنه لا وجه لاعتبارها، والعلمية تشاركها في كونها في الاسم في الأصل، وترجح عليها بقرب العهد والقوة.",
     "en": "What indicates that it is the more evident has already preceded. Among the things that necessitate it is that the original proper-nounhood is precluded from being reckoned, because there is no ground for reckoning it; while proper-nounhood shares with it (descriptiveness) in being, in origin, within the noun, and outweighs it by recency [of establishment] and strength."},
]
