# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 123 (printed ١٢٢)."""

PAGE_NUMBER = 123
PRINTED_PAGE = "١٢٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "لجواز ورود «اصمت» بكسرتين، وإن لم يشتهر، فالأوزان التي تحقق فيها العدل تحقيقا كان أو تقديرا لم تجامع وزن الفعل.",
     "en": "because of the permissibility that “iṣmit” may occur with two kasras, even if this is not well known; for the patterns in which deviation (ʿadl) is realized — whether realized in fact or by estimation — do not coincide with the pattern of the verb."},
    {"type": "matn",
     "ar": "وأيضا قد عرفت[[١]] فيما تقدم أن مجرد وجود أصل محقق لا يكفي في اعتبار العدل التحقيقي بدون اقتضاء منع الصرف إياه، واعتبار خروج الصيغة عن ذلك الأصل، وههنا لا يقتضيه؛ لوجود سببين في «اصمت» وراء العدل، وهما العلمية والتأنيث.",
     "en": "Moreover, you have already learned in what preceded that the mere existence of a realized base form does not suffice for reckoning true deviation (al-ʿadl al-taḥqīqī) unless the prevention of full inflection (manʿ al-ṣarf) calls for it, together with the reckoning of the form’s departure from that base; and here it does not call for it, because in “iṣmit” there are two causes over and above deviation — namely proper-nounhood (ʿalamiyya) and feminineness (taʾnīth)."},
    {"type": "matn",
     "ar": "ثم إنه أشار إلى استثناء مثل: «أحمر» علما إذا نكر عن هذه القاعدة على قول سيبويه بقوله: (وخالف سيبويه الأخفش) الأخفش المشهور، هو أبو الحسن، تلميذ سيبويه.",
     "en": "Then he alluded to the exception, from this rule, of the like of “aḥmar” when used as a proper name and then made indefinite, according to the doctrine of Sībawayh, in his statement: (And al-Akhfash differed from Sībawayh). The famous al-Akhfash is Abū al-Ḥasan, the pupil of Sībawayh."},
    {"type": "matn",
     "ar": "ولما كان قول التلميذ أظهر[[٢]] مع موافقته لما ذكره من القاعدة جعله أصلا، وأسند المخالفة إلى الأستاذ[[٣]]، وإن كان غير مستحسن تنبيها على ذلك (في) انصراف (نحو: أحمر علما[[٤]]) والمراد: بـ«نحو: أحمر» ما كان معنى الوصفية فيه، قبل العلمية ظاهرا غير خفي، فيدخل فيه سكران وأمثاله.",
     "en": "Since the pupil’s doctrine was the more evident, together with its agreement with the rule he had stated, he made it the base and ascribed the divergence to the master — even though [the master] is the more approved — so as to draw attention to that: (in) the full inflection of (the like of: “aḥmaru” [when made] a proper name). What is meant by “the like of ‘aḥmar’” is that in which the sense of descriptiveness (waṣfiyya), prior to proper-nounhood, was manifest and not hidden; so “sakrān” (drunken) and its like fall under it."},
    {"type": "matn",
     "ar": "ويخرج عنه «أفعل» للتأكيد نحو: «أجمع»، فإنه منصرف عند التنكير بالاتفاق؛ لضعف معنى الوصفية فيه[[٥]] قبل العلمية، لكونه بمعنى «كل»، وكذلك أفعل التفضيل[[٦]] المجرد عن «من» التفضيلية، فإنه بعد التنكير منصرف بالاتفاق؛ لضعف معنى الوصفية فيه، حتى صار «أفعل» اسما[[٧]]، وإن كان معه «من»، فلا ينصرف بلا خلاف؛ لظهور معنى الوصفية فيه بسبب «من» التفضيلية.",
     "en": "Excluded from it is “afʿal” used for corroboration, such as “ajmaʿ,” for it is fully inflected when made indefinite by agreement, on account of the weakness of the sense of descriptiveness in it prior to proper-nounhood, since it has the meaning of “all” (kull); and likewise the elative “afʿal” (afʿal al-tafḍīl) when stripped of the comparative “min,” for after being made indefinite it is fully inflected by agreement, on account of the weakness of the sense of descriptiveness in it, to the point that “afʿal” became a noun; but if “min” accompanies it, it is not fully inflected, without dispute, because of the manifestness of the sense of descriptiveness in it by reason of the comparative “min.”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "به يندفع النقض بآخر على وزن أفعل حيث قيل: إنه معدول عما كان معه اللام أو الإضافة أو «من».",
     "en": "By this the objection is repelled that is raised through “ākhar,” which is of the pattern afʿal, where it was said: it is deviated from that which had with it the definite article (lām), or the genitive construction (iḍāfa), or “min.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يبعد أن يجعل الأخفش فاعلا؛ إذ يلزم حينئذ جعل قول سيبويه أصلا مع أنه مناف للقاعدة الحقة عنده، وامتناع النصب اعتبارا بتقدير اللام.",
     "en": "It is far-fetched to make al-Akhfash the agent [of the verb “differed”], for that would then entail making Sībawayh’s doctrine the base, even though it contradicts the correct rule in his view, and would entail the impossibility of the accusative on the consideration of an implied lām."},
    {"type": "pair",
     "ar": "والقول بأنه منصوب على الظرفية، أو الحالية، أو كونه بدل الاشتمال بعيد.",
     "en": "And the view that it is in the accusative as an adverbial (ẓarfiyya), or as a circumstantial qualifier (ḥāliyya), or as an inclusive substitution (badal al-ishtimāl), is remote."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا مبني على أن فاعل المخالفة من هو البادي للفعل وإن كان مفعولها أيضا فاعلا ضمنا.",
     "en": "This is built upon [the premise] that the agent of the divergence is the one who initiates the act, even though its object too is implicitly an agent."},
    {"type": "pair",
     "ar": "ثم إن الأستاذ لفظ مركب أعجمي بمعنى المعلم والماهر في صنعته، وليس بعربي؛ إذ لا يوجد كلمة عربية اجتمع فيها السين والذال.",
     "en": "Then “al-ustādh” is a compound non-Arabic word meaning the teacher and the one skilled in his craft; it is not Arabic, for no Arabic word is found in which sīn and dhāl come together."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "حال، والعامل هي المماثلة أو المخالفة. وعلى الثاني ذو الحال، نحو: أو ما أضيف إليه كما في قوله تعالى:",
     "en": "[It is] a circumstantial qualifier (ḥāl), and the governor is [the notion of] likeness or of divergence. On the second [consideration], the possessor of the state (dhū al-ḥāl) is “the like of…,” or that to which it is annexed, as in His words, the Exalted:"},
    {"type": "quran",
     "ar": "﴿واتبع ملة إبراهيم حنيفا﴾ (سورة النساء:١٢٥).",
     "en": "“…and follows the creed of Ibrāhīm, inclining truly [to faith] (ḥanīfan)” (Qurʾān, Sūrat al-Nisāʾ 4:125)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بخلاف أفعل فعلاء. ولذا لا يعمل أفعل التفضيل في الظاهر دون أفعل فعلاء.",
     "en": "Unlike the “afʿal” whose feminine is “faʿlāʾ.” For this reason the elative “afʿal” does not govern an overt noun, unlike the “afʿal” whose feminine is “faʿlāʾ.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ولذا لا يعمل في الظاهر بخلاف مثل: أحمر.",
     "en": "For this reason it does not govern an overt noun, unlike the like of “aḥmar.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: كاسم أفعل الخالي عن الصفة كأرنب مثلا.",
     "en": "That is: like the noun “afʿal” that is devoid of descriptiveness, such as “arnab” (hare), for example."},
]
