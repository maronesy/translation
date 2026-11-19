# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 172 (printed ١٧١)."""

PAGE_NUMBER = 172
PRINTED_PAGE = "١٧١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "أي: «هو أهل الحمد»، وإنما وجب حذفه ليعلم[[١]] أنه كان في الأصل صفة، فقطع لقصد المدح أو الذم أو غير ذلك،",
     "en": "…that is: “He is the One worthy of praise.” Its elision is obligatory only so that it may be known that it was originally an adjective (ṣifa), and was cut off with the intent of praise, blame or the like;"},
    {"type": "matn",
     "ar": "فلو ظهر المبتدأ لم يتبين ذلك القصد.",
     "en": "for if the subject were made overt, that intent would not be apparent."},
    {"type": "matn",
     "ar": "ويجب حذفه أيضا عند من قال في «نعم الرجل زيد»: إن تقديره: «هو زيد».",
     "en": "Its elision is likewise obligatory according to those who say of “What an excellent man Zayd is” (niʿma al-rajulu Zaydun) that its implied form is: “He is Zayd.”"},
    {"type": "matn",
     "ar": "(كقول المستهل) أي: المبتدأ المحذوف جوازا مثل المبتدأ المحذوف في مقول المستهل المبصر للهلال[[٢]] الرافع صوته عند إبصاره (الهلال والله) أي: «هذا الهلال والله» بالقرينة الحالية[[٣]]،",
     "en": "(As in the words of the one sighting the new moon—ka-qawli al-mustahilli), that is: the subject elided optionally is like the subject elided in what is said by the one sighting the new moon, who sees the crescent and raises his voice on seeing it: (“The crescent, by Allah!”—al-hilālu wa-llāhi), that is: “This is the crescent, by Allah,” by the indicator of the situation (al-qarīna al-ḥāliyya)."},
    {"type": "matn",
     "ar": "وليس من باب حذف الخبر بتقدير: «الهلال هذا»؛",
     "en": "It does not belong to the category of eliding the predicate, with the implied form “The crescent is this”;"},
    {"type": "matn",
     "ar": "لأن مقصود المستهل تعيين شيء[[٤]] بالإشارة والحكم عليه بالهلالية، ليتوجه إليه الناظرون ويروه كما يراه،",
     "en": "because what the one sighting the moon intends is to specify a thing by pointing and to judge of it that it is the crescent, so that the onlookers turn toward it and see it as he sees it."},
    {"type": "matn",
     "ar": "وإنما أتى بالقسم جريا على عادة المستهلين غالبا، ولئلا يتوهم[[٥]] نصب الهلال عند الوقف.",
     "en": "He added the oath only in keeping with the usual habit of those who sight the moon, and so that the accusative of “al-hilāl” would not be supposed when pausing (ʿinda al-waqf)."},
    {"type": "matn",
     "ar": "(و) قد يحذف (الخبر جوازا) أي: حذفا جائزا، لقيام قرينة من غير إقامة شيء مقامه",
     "en": "(And the predicate) may be elided (optionally—wa-al-khabaru jawāzan), that is: as a permissible elision, when an indicator is present, without anything being put in its place;"},
    {"type": "matn",
     "ar": "(مثل) الخبر المحذوف جوازا في قولك: (خرجت فإذا السبع[[٦]])،",
     "en": "(like) the predicate elided optionally in your saying: (“I went out, and lo, the beast of prey!”—kharajtu fa-idhā al-sabuʿu);"},
    {"type": "matn",
     "ar": "فإن تقديره على المذهب الصحيح كما نص عليه صاحب اللباب: «خرجت فإذا السبع واقف»،",
     "en": "for its implied form according to the correct doctrine, as the author of al-Lubāb stated explicitly, is: “I went out, and lo, the beast of prey was standing,”"},
    {"type": "matn",
     "ar": "على أن يكون «إذا» ظرف زمان للخبر المحذوف من غير ساد مسده، أي: «ففي وقت خروجي السبع واقف».",
     "en": "with “idhā” being an adverb of time (ẓarf zamān) for the elided predicate, with nothing filling its place; that is: “At the time of my going out, the beast of prey was standing.”"},
    {"type": "matn",
     "ar": "(و) قد يحذف الخبر لقيام قرينة (وجوبا) أي: حذفا واجبا (فيما التزم[[٧]]) أي:",
     "en": "(And) the predicate may be elided when an indicator is present (obligatorily—wujūban), that is: as an obligatory elision, (in what has been made binding—fī-mā ultuzima), that is:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "حاصل الكلام: أنه صفة لما قبله في المعنى، لكنه قطع عنه، وجعل إعرابه مخالفا لإعراب ما قبله؛",
     "en": "The upshot is: it is an adjective of what precedes it in meaning, but it has been cut off from it, and its inflection has been made to differ from the inflection of what precedes it;"},
    {"type": "pair",
     "ar": "لأن في الافتنان وتغيير المألوف زيادة تنبيه، وإيقاظا للسامع للإصغاء إليه.",
     "en": "because in varying the mode of expression (iftinān) and altering what is customary there is added alerting, and a rousing of the listener to attend to it."},
    {"type": "pair",
     "ar": "وذلك إنما يكون لشدة الاهتمام به، وشدة الاهتمام بمدح أو ذم أو ترحم، يعتني به زيادة اعتناء،",
     "en": "That happens only out of intense concern with it, and the intense concern is with praise, blame or commiseration (taraḥḥum), to which he gives added attention;"},
    {"type": "pair",
     "ar": "فكأنه أراد أنه امتاز من بين الصفات بالمدح أو الذم أو الترحم،",
     "en": "so it is as though he meant that it stands out from among the attributes by praise, blame or commiseration."},
    {"type": "pair",
     "ar": "ولو ذكر المبتدأ لم يبق في صورة الوصف، فلم يتبين أنه في الأصل وصف ثم غير.",
     "en": "Were the subject mentioned, it would not remain in the form of a qualification, and it would not be apparent that it was originally a qualification and was then altered."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "صفة كاشفة لقوله: المستهل؛ لأن معناه الطالب لرؤية الهلال، والإبصار الرؤية،",
     "en": "[“Seeing the crescent” is] an explicative adjective (ṣifa kāshifa) for his word “al-mustahill,” because its meaning is “the one seeking to sight the crescent,” and seeing (ibṣār) is sighting;"},
    {"type": "pair",
     "ar": "ومن هذا القبيل: ﴿من عمل صالحا فلنفسه﴾ (سورة فصلت: ٤٦)، أي: فعمله لنفسه.",
     "en": "and of this kind is: “Whoever does good, it is for himself” (Qurʾān, Sūrat Fuṣṣilat 41:46), that is: “his deed is for himself.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وهي حالة كون القائل مبصرا للهلال.",
     "en": "It is the situation of the speaker’s seeing the crescent."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا تعيين الهلال بالإشارة.",
     "en": "Not specifying the crescent by pointing."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "نصب الهلال بـ«رأيت أو أرى». وذلك لأن الأصل في المفردات الوقف.",
     "en": "The accusative of “al-hilāl” by [an implied] “I saw” or “I see.” That is because the default for single words is the pause (waqf)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الفاء للعطف حملا على المعنى، أي: خرجت ففاجأت كذا،",
     "en": "The fāʾ is conjunctive, construed according to the meaning, that is: “I went out and came upon such-and-such.”"},
    {"type": "pair",
     "ar": "وقيل: جواب الشرط، ولعله أراد بهما لزوم ما بعدها لما قبلها، أي: مفاجأة السبع لازمة لخروجي.",
     "en": "It has been said: [it introduces] the apodosis of a condition; perhaps by these two he meant that what follows it is entailed by what precedes it, that is: coming upon the beast of prey was entailed by my going out."},
    {"type": "pair",
     "ar": "وقيل: زائدة، وفيه أنه لا يجوز حذفها.",
     "en": "It has also been said: it is redundant (zāʾida); against this, its omission is not permitted."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يقال: ألزمته الشيء فالتزمه، أي: قبل ملازمته.",
     "en": "One says: “I made the thing binding on him, and he bound himself to it (iltazamahu),” that is: he accepted adhering to it."},
]
