# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 219 (printed ٢١٨)."""

PAGE_NUMBER = 219
PRINTED_PAGE = "٢١٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(فإن كان في آخره) أي: آخر المنادى (زيادتان) كائنتان (في حكم) الزيادة (الواحدة) في أنهما زيدتا معا.",
     "en": "(If there are at its end)—that is, at the end of the vocative—(two additions) that are (in the status of a single) addition, in that the two were added together,"},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «ثمانية ومرجانة»، فإن الياء والنون فيهما زيدتا أولا، ثم زيدت تاء التأنيث، فلم يحذف منهما إلا الآخر",
     "en": "—by this he guarded against such as “thamāniya” and “Marjāna,” for the yāʾ and the nūn in them were added first and then the feminine tāʾ was added, so only the last is dropped from them—"},
    {"type": "matn",
     "ar": "(كأسماء) إذا جعلتها «فعلاء» من الوسامة أي: الحسن كما هو مذهب سيبويه لا «أفعالا» لا جمع «اسم» على ما هو مذهب غيره؛ لأنه يكون حينئذ من باب «عمار»[[١]]",
     "en": "(as in “Asmāʾ”) when you take it as faʿlāʾ from wasāma, that is, beauty, as is Sībawayh’s position—not as afʿāl, the plural of “ism,” as is the position of others, because it would then belong to the pattern of “ʿAmmār”—"},
    {"type": "matn",
     "ar": "(و«مروان») أو كان في آخره (حرف صحيح) أي: صحيح أصلي[[٢]]، لتبادره إلى الذهن؛ لأن الغالب في الحرف الصحيح الأصالة،",
     "en": "(and “Marwān”); or if there is at its end (a sound letter), that is, a sound root letter—since this is what comes first to mind, because a sound letter is mostly a root letter."},
    {"type": "matn",
     "ar": "فيخرج منه نحو: «سعلاة»؛ لأنه لا يحذف منه إلا التاء،",
     "en": "So such as “siʿlāh” is excluded by it, because only the tāʾ is dropped from it."},
    {"type": "matn",
     "ar": "وهو أعم[[٣]] من أن يكون حقيقة أو حكما، فيشمل مثل: «مرمي ومدعو»، فإن الحرف الأخير منهما في حكم الصحيح في الأصالة[[٤]]",
     "en": "It is more general than being so really or by status, so it includes such as “marmiyy” and “madʿuww,” for the last letter of each is in the status of the sound [letter] as regards being a root letter—"},
    {"type": "matn",
     "ar": "(قبله مدة) أي: «ألف، أو واو، أو ياء» ساكنة[[٥]] حركة ما قبلها من جنسها[[٦]]،",
     "en": "(preceded by a long vowel—madda), that is, an alif, wāw or yāʾ that is quiescent, the vowel before it being of its own kind;"},
    {"type": "matn",
     "ar": "والمراد بها المدة الزائدة لتبادرها إلى الذهن؛ لغلبتها وكثرتها[[٧]]، فيخرج منه نحو: «مختار»، فإنه لا يحذف منه[[٨]] إلا الحرف الأخير",
     "en": "what is meant by it is the added madda, since it comes first to mind because it predominates and is frequent; so such as “Mukhtār” is excluded by it, for only the last letter is dropped from it—"},
    {"type": "matn",
     "ar": "(وهو) أي: والحال أن ما في آخره حرف صحيح قبله مدة (أكثر من أربعة أحرف) من الحروف كـ«منصور وعمار ومسكين»، لئلا يلزم من حذف حرفين منه عدم بقائه على أقل أبنية المعرب،",
     "en": "(and it is), that is, the case being that the word ending in a sound letter preceded by a madda is, (more than four letters), as in “Manṣūr,” “ʿAmmār” and “Miskīn,” so that dropping two letters from it does not leave it short of the smallest pattern of the declinable noun—"},
    {"type": "matn",
     "ar": "وإنما لم يأخذ هذا القيد[[٩]] في قوله: «زيادتان في حكم الواحدة»؛ لأن نحو: «ثبون وقلون» يرخم بحذف زيادته؛ لأن بقاء الكلمة فيه",
     "en": "He did not take this qualification into his words “two additions in the status of a single one,” only because such as “thubūn” and “qullūn” is curtailed by dropping its addition, because the word’s remaining in it…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في أن في آخره حرفا صحيحا قبله مدة، فهو حينئذ أيضا من قبيل ما يحذف منه حرفان عند الترخيم، لكن من الضابطة الثانية دون الأولى.",
     "en": "In that at its end is a sound letter preceded by a madda; so it too then belongs to what loses two letters in curtailment, but under the second rule, not the first."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لو أراد عن الحرف الأصلي سواء كان حرف علة، أو لم يكن ليشمل مثل مرمي ومدعو، فلا يحتاج إلى التعميم من الحقيقي والحكمي،",
     "en": "Had he meant by it the root letter, whether a weak letter or not, so as to include such as “marmiyy” and “madʿuww,” there would be no need for generalizing over the real and the status-based;"},
    {"type": "pair",
     "ar": "لكن أراد أن يصحح لفظ الصحيح بقدر الإمكان.",
     "en": "but he wanted to keep the word “ṣaḥīḥ” (sound) valid as far as possible."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما عم؛ لأن ترخيم مثل مدعو ومرمي بحذف الحرف الأخير والمدة السابقة.",
     "en": "He generalized only because such as “madʿuww” and “marmiyy” are curtailed by dropping the last letter and the preceding madda."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أو في صحة إجراء الإعراب عليه يوافقه ما قيل من أن مثل: دلو وظبي ملحق بالاسم الصحيح لصحة إجراء الإعراب عليه.",
     "en": "Or in its validly carrying the iʿrāb. This agrees with what has been said: that such as “dalw” and “ẓaby” are attached to the sound noun because they validly carry the iʿrāb."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "احتراز عن نحو كنهور على وزن سفرجل عظيم السحاب",
     "en": "A guard against such as “kanahwar,” on the pattern of safarjal—a great cloud—"},
    {"type": "pair",
     "ar": "ومشيرف على وزن مدحرج، أي: مقطوع شريافه، وهو ورق الزرع إذا طال وكثر حتى يخاف فساده فيقطع.",
     "en": "and “mushayraf,” on the pattern of mudaḥraj, that is, [a crop] whose shiryāf has been cut: that is the leaves of a crop when they grow long and abundant until its spoiling is feared, so they are cut."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "احترز به عن نحو: رجيل وسنور، فإنهما لا يسمى مدة.",
     "en": "By it he guarded against such as “rujayl” and “sinnawr,” for these are not called madda."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أو المراد ما هو مدة مطلقا، وألف مختار لم يكن في أصله مدة، وإنما صار مدة بالإعلال.",
     "en": "Or what is meant is whatever is a madda absolutely; and the alif of “Mukhtār” was not a madda in origin, but became one only through iʿlāl."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "خلافا للأخفش، فإنه يحذف المدة أيضا.",
     "en": "Contrary to al-Akhfash, for he drops the madda as well."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "ولك أن تأخذه فيهما، وتجعل ثبون أكثر من أربعة أحرف في الأصل.",
     "en": "You may also take it in both, and treat “thubūn” as more than four letters in origin…"},
]
