# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 52 (printed ٥١)."""

PAGE_NUMBER = 52
PRINTED_PAGE = "٥١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (continued from p. ٥٠) ----------------
    {"type": "matn",
     "ar": "في نفسه، لا باعتبار أمر خارج عنه، كقولك: «الدار في نفسها حكمها كذا» أي: لا باعتبار أمر خارج عنها. ولذلك قيل: الحرف ما دل على معنى في غيره، أي: حاصل في غيره، أي: باعتبار متعلقه[[١]]، لا باعتباره[[٢]] في نفسه[[٣]]» انتهى كلامه[[٤]].",
     "en": "…in itself, not by consideration of some matter external to it — as when you say: «the house, in itself, its ruling is such-and-such», that is, not by consideration of a matter outside it. It is for this reason that it is said: the ḥarf (particle) is that which indicates a meaning in something other than itself — that is, obtaining in something other than itself — that is, by consideration of its correlate (mutaʿallaq)[[١]], not by consideration of it[[٢]] in itself[[٣]].” His words end here[[٤]]."},
    {"type": "matn",
     "ar": "ومحصوله[[٥]]: ما ذكره بعض المحققين[[٦]] حيث قال: كما أن في الخارج موجودا قائما بذاته[[٧]]، وموجودا قائما بغيره[[٨]]، كذلك في الذهن معقول[[٩]] هو مدرك قصدا",
     "en": "Its upshot[[٥]] is what one of the verifying scholars (al-muḥaqqiqūn)[[٦]] mentioned when he said: just as in external reality there is an existent subsisting by itself[[٧]] and an existent subsisting by another[[٨]], so too in the mind there is an intelligible[[٩]] that is apprehended intentionally (qaṣdan),"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يجوز بفتح اللام وكسرها، وهو السير والبصرة في قولك: سرت من البصرة؛ لأن «من» ههنا دال على معنى، وهو الابتداء الحاصل في السير باعتبار الحال، والبصرة باعتبار المحل.",
     "en": "It is permissible with a fatḥa or a kasra on the lām [i.e., mutaʿallaq]; and it is the journey (al-sayr) and Basra (al-Baṣra) in your saying “I set out from Basra,” for «min» here indicates a meaning — namely the inception (al-ibtidāʾ) obtaining in the journey by consideration of the state (al-ḥāl), and in Basra by consideration of the locus (al-maḥall)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: باعتبار المعنى.",
     "en": "That is: by consideration of the meaning."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: في نفس الحرف. الجار متعلق باعتباره.",
     "en": "That is: in the ḥarf itself. The governing particle (al-jārr) is connected [to it] by consideration of it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: كلام المصنف في الإيضاح.",
     "en": "That is: the words of the author in al-Īḍāḥ."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: محصل كلام المصنف في الإيضاح ونتيجته.",
     "en": "That is: the distilled sense of the author’s words in al-Īḍāḥ and its conclusion."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يعني السيد الشريف في حاشية المطول، كأنه أراد الشارح التنبيه على أن هذا التحقيق ليس من السيد الشريف كما هو المشهور، بل أخذه من كلام المصنف، وليس كما ظنه؛",
     "en": "He means al-Sayyid al-Sharīf in his gloss on al-Muṭawwal. It is as though the commentator intended to draw attention to the fact that this verification is not al-Sayyid al-Sharīf’s own — as is commonly held — but rather that he took it from the author’s words; yet it is not as he supposed;"},
    {"type": "pair",
     "ar": "لأن الناظر في كلام الإيضاح يعرف أن المصنف بعيد عن هذا التحقيق، وإن كان عبارته الجملة المنقولة وقعت اتفاقا بحيث يحتمل التفصيل بهذا التحقيق.",
     "en": "for one who examines the wording of al-Īḍāḥ knows that the author is far from this verification, even though his expression — the transmitted sentence — happened, by chance, to be such as could admit the detail by this verification."},
    {"type": "pair",
     "ar": "كيف وقد ذكر أن الفرق بين الأسماء اللازمة الإضافة والحروف أن الواضع شرط في دلالة الحروف على معناه ذكر المتعلق، ولم يشترط ذلك في الأسماء اللازمة الإضافة، وإنما التزم الإضافة لغرض آخر غير كون دلالتها مشروطة بذكر المضاف إليه.",
     "en": "How could it be otherwise, when he has stated that the difference between nouns that necessarily require annexation and the particles is that the positer stipulated, for the particles’ signification of their meaning, the mention of the correlate, but did not stipulate that for nouns that necessarily require annexation; rather he made annexation obligatory for another purpose, not because their signification is conditioned upon mentioning the term of annexation (al-muḍāf ilayhi)."},
    {"type": "pair",
     "ar": "ولا خفاء في أنه بعد الوضع، ولا دخل للوضع في الدلالة حتى يكون بشرطه متوقفا على ذكر المتعلق.",
     "en": "and there is no obscurity in that, after the positing [is done], the positing has no bearing on signification such that, by its condition, it would depend upon mentioning the correlate (al-mutaʿallaq)."},
    {"type": "pair",
     "ar": "فلو كان صاحب هذا التحقيق لم يصدر منه مثل هذا الكلام، بل المصنف أيضا يستحق أن يقال في حقه ما قاله السيد المحقق في حق نجم الأئمة حيث قال في حواشي شرحه على الكافية في هذا المقام: يقرب من تحقيق معنى الحرف تارة، ويبعد عنه بمراحل تارة أخرى.",
     "en": "For had the author of this verification been one from whom the like of these words had not issued [that would be excusable]; rather the author too deserves to have said of him what the verifying Sayyid said of Najm al-Aʾimma, where he said in the glosses of his commentary on al-Kāfiya, in this very passage: “At times he draws near to verifying the meaning of the ḥarf, and at times he departs from it by leagues.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: كما أن الموجود الخارجي قد يكون وصفا لأمر تابعا له، وقد لا يكون، كذلك الموجود في الذهن قد يكون تابعا لأمر في الملاحظة، وقد لا يكون. وفيه تشبيه المعقول بالمحسوس.",
     "en": "That is: just as the externally-existent may be a description of a thing, dependent upon it, and may not be, so too the mentally-existent may be dependent upon a thing in [the act of] observation, and may not be. Herein is a likening of the intelligible to the sensible."},
    {"type": "pair",
     "ar": "ويظهر منه وجه آخر لاستعمال لفظة «في»، وهو أنه لما شابه المعنى الحرفي التابع لأمر العرض القائم بالجوهر التابع له، صح أن ينسب إلى ذلك الأمر بلفظة «في»، كما ينسب العرض إلى محله بلفظة «في».",
     "en": "From it a further ground appears for using the word «fī» (in): namely that, since the particle-meaning — which is dependent upon a thing — resembles the accident subsisting in the substance dependent upon it, it is sound to relate it to that thing by the word «fī», just as the accident is related to its locus by the word «fī»."},
    {"type": "pair",
     "ar": "والمعنى المستقل لما شابه الجوهر صح أن يقال: إنه كائن في نفسه بمعنى أنه لم يكن في غيره، كما يقال: إن الجوهر قائم بذاته بمعنى أنه غير قائم بغيره.",
     "en": "And the independent meaning, since it resembles the substance, may soundly be said [to be]: «it is subsisting in itself», meaning that it is not in another — just as it is said: «the substance subsists by itself», meaning that it is not subsisting by another."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لو قيل: كما أن في الخارج موجودا قائما بذاته هو موجود في ذاته، وموجودا قائما بغيره هو موجود في غيره، لكان غاية في إيضاح معنى الحرف وما يقابله، وتنويرا تاما لاستعمال «في» في الحدود الثلاثة،",
     "en": "Had it been said: “just as in external reality there is an existent subsisting by itself that is existent in its essence, and an existent subsisting by another that is existent in another,” it would have been the utmost in clarifying the meaning of the ḥarf and its opposite, and a complete illumination for using «fī» in the three definitions;"},
    {"type": "pair",
     "ar": "فإن «في» في قولهم: «السواد في زيد» ليس كما في قولهم: «الماء في الكوز»، بل بمعنى الاعتبار، وللدلالة على أن وجود السواد ليس إلا باعتبار المحل، كما أن معنى الموجود في نفسه لا في غيره باعتبار غيره.",
     "en": "for «fī» in their statement “blackness is in Zayd” is not like it in their statement “water is in the jug”; rather it has the sense of consideration (iʿtibār), and signifies that the existence of blackness is only by consideration of the locus — just as the meaning of “existent in itself, not in another” is by consideration of the other."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "الأولى معلوم. ولا يذهب عليك التفاوت بين المشبه والمشبه به بأن القائم بذاته لا يصير قائما بغيره، والقائم بغيره لا يصير قائما بذاته، بخلاف المدرك قصدا والمدرك تبعا، فربما يقصد إلى المدرك تبعا، فيصير مدركا قصدا، وبالعكس.",
     "en": "The first [case] is evident. Nor should the disparity between the likened (al-mushabbah) and that to which it is likened (al-mushabbah bihi) escape you — in that what subsists by itself does not become subsisting by another, and what subsists by another does not become subsisting by itself — unlike the intentionally-apprehended and the dependently-apprehended, for the dependently-apprehended may [come to be] intended, thereby becoming apprehended intentionally, and vice versa."},
]
