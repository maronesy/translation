# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 214 (printed ٢١٣)."""

PAGE_NUMBER = 214
PRINTED_PAGE = "٢١٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # REVIEW: the closing guillemet after «من قبلي» has no opening guillemet on this page; transcribed as printed.
    {"type": "matn",
     "ar": "والبيت لجرير حين أراد عمر التيمي الشاعر أن يهجوه، فقال جرير خطابا لبني تيم: لا تتركوا عمر أن يهجوني فيلقينكم في سوءة -أي: مكروه- من قبلي»، يعني: مهاجاته إياهم.",
     "en": "The verse is by Jarīr, [composed] when the poet ʿUmar al-Taymī wanted to satirize him; so Jarīr said, addressing the Banū Taym: “Do not let ʿUmar satirize me, lest he cast you into an evil (sawʾa)—that is, something hateful—on my account,” meaning: [Jarīr’s] satirizing them in return."},

    {"type": "section", "ar": "[المنادى المضاف إلى ياء المتكلم]",
     "en": "The Vocative Annexed to the First-Person yāʾ"},

    {"type": "matn",
     "ar": "(و) المنادى (المضاف إلى ياء المتكلم يجوز فيه) وجوه أربعة:",
     "en": "(And) the vocative (annexed to the yāʾ of the speaker admits) four forms:"},
    {"type": "matn",
     "ar": "١-فتح الياء[[١]]، مثل: (يا غلامي).",
     "en": "1. Giving the yāʾ a fatḥa, as in: (yā ghulāmiya, “O my servant”)."},
    {"type": "matn",
     "ar": "٢-وسكونها[[٢]]، مثل: (يا غلامي).",
     "en": "2. Its being quiescent (sukūn), as in: (yā ghulāmī)."},
    {"type": "matn",
     "ar": "٣-وسقوط الياء اكتفاء بالكسرة[[٣]] إذا كان قبله كسرة؛ احترازا عن نحو: «يا فتاي» مثل: (يا غلام).",
     "en": "3. Dropping the yāʾ, the kasra sufficing [in its place], when a kasra precedes it—guarding against such as “yā fatāya” (O my youth)—as in: (yā ghulāmi)."},
    {"type": "matn",
     "ar": "٤-وقلبها ألفا[[٤]] مثل: (يا غلاما).",
     "en": "4. Changing it into an alif, as in: (yā ghulāmā)."},
    {"type": "matn",
     "ar": "وهذان الوجهان يقعان غالبا في النداء؛ لأن النداء موضع تخفيف؛ لأن المقصود غيره، فيقصد الفراغ من النداء بسرعة، ليتخلص منه ويتوجه إلى المقصود من الكلام،",
     "en": "These two [last] forms occur mostly in the vocative, because the vocative is a place of lightening: what is intended is something other than it, so one aims to be done with the vocative quickly, to be free of it and turn to what is intended by the utterance."},
    {"type": "matn",
     "ar": "فخفف «يا غلامي» بوجهين -حذف الياء وإبقاء الكسرة دليلا عليه وقلب الياء ألفا- لأن الألف والفتحة أخف من الياء والكسرة،",
     "en": "So “yā ghulāmī” was lightened in two ways—dropping the yāʾ while keeping the kasra as an indication of it, and changing the yāʾ into an alif—because the alif and the fatḥa are lighter than the yāʾ and the kasra."},
    {"type": "matn",
     "ar": "وهما أي: -هذان الوجهان- وإن كانا واقعين في المنادى المضاف إلى ياء المتكلم، لكن لا يقعان في كل منادى كذلك،",
     "en": "And these two—that is, these two forms—although they occur in the vocative annexed to the yāʾ of the speaker, do not occur in every vocative of that kind,"},
    {"type": "matn",
     "ar": "بل فيما غلب عليه الإضافة إلى ياء المتكلم، واشتهر بها لتدل الشهرة على الياء المغيرة بالحذف أو القلب،",
     "en": "but only in one that is predominantly annexed to the yāʾ of the speaker and well known for it, so that this familiarity points to the yāʾ altered by elision or by change;"},
    {"type": "matn",
     "ar": "فلا تقول: «يا عدو، ويا عدوا»، وقد جاء شاذا[[٥]] في المنادى «يا غلام» بالفتح اكتفاء بالفتحة عن الألف.",
     "en": "so you do not say “yā ʿaduwwi” or “yā ʿaduwwā” (O my enemy). It has occurred anomalously (shādhdhan) in the vocative “yā ghulāma” with the fatḥa, the fatḥa sufficing in place of the alif."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وهو الأصل كما هو المشهور، والسكون أكثر.",
     "en": "This is the original form, as is well known, though the sukūn is more frequent."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهو الأكثر.",
     "en": "This is the more frequent."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وقد يضم، وذلك في الاسم الغالب عليه الإضافة إلى الياء للعلم بالمراد.",
     "en": "It may also take a ḍamma; that is in a noun predominantly annexed to the yāʾ, since what is meant is known."},
    {"type": "pair",
     "ar": "ومنه القراءة الشاذة: ﴿رب احكم﴾، بضم الباء.",
     "en": "Of this is the non-canonical reading (al-qirāʾa al-shādhdha) “Rabbu-ḥkum” (My Lord, judge) [translator’s reference: cf. Qurʾān, Sūrat al-Anbiyāʾ 21:112], with a ḍamma on the bāʾ."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "روما للخفة ولامتداد الصوت ورفعه المناسب للنداء.",
     "en": "Seeking lightness, and the prolonging and raising of the voice that suits the vocative."},
    {"type": "pair",
     "ar": "قيل: هذه لغة طي، فإنهم يبدلون الياء الواقعة بعد الكسرة ألفا، فيقال في بقي وفني بقا وفنا، وفي جارية وناصية جاراة وناصاة.",
     "en": "It has been said: this is the dialect of Ṭayyiʾ, for they replace a yāʾ coming after a kasra with an alif; so for baqiya and faniya one says baqā and fanā, and for jāriya and nāṣiya, jārāh and nāṣāh."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: أما فتح يا بني، والأصل يا بنيا فليس بشاذ، كما شذ في يا غلام لاجتماع يائين.",
     "en": "Shaykh al-Raḍī said: as for the fatḥa of “yā bunayya,” the original being “yā bunayyā,” it is not anomalous as it is anomalous in “yā ghulāma,” because of the meeting of two yāʾs."},
]
