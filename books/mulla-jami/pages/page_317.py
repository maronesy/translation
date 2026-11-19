# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 317 (printed ٣١٦)."""

PAGE_NUMBER = 317
PRINTED_PAGE = "٣١٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وذلك يحتمل على معنيين:» at the foot of PDF p. 316.
    {"type": "matn",
     "ar": "أحدهما: أن يكون الوقت مقدرا في نظم الكلام، ويكون المسجد مضافا إليه، والجامع صفة للوقت،",
     "en": "The first: that “time” is supplied in the structure of the utterance, the mosque being annexed to it and “al-jāmiʿ” being an adjective of the time;"},
    {"type": "matn",
     "ar": "فيندفع الإيراد بوجهين، فإن الجامع ليس مضافا إليه ولا صفة للمضاف.",
     "en": "the objection is then removed on two counts, for “al-jāmiʿ” is neither the term annexed to nor an adjective of the annexed term."},
    {"type": "matn",
     "ar": "وثانيهما[[١]]: أن يكون «الوقت» محذوفا، و«الجامع» قائما مقامه منطويا عليه، فيكون بمنزلة الصفات الغالبة، فيضاف «المسجد» إليه،",
     "en": "The second: that “time” is elided and “al-jāmiʿ” stands in its place, enfolding it, so that it is like the predominant adjectives (al-ṣifāt al-ghāliba), and “al-masjid” is annexed to it;"},
    {"type": "matn",
     "ar": "فيندفع الإيراد بوجه واحد، وهو أن الجامع ليس صفة للمضاف.",
     "en": "the objection is then removed on one count, namely that “al-jāmiʿ” is not an adjective of the annexed term."},
    {"type": "matn",
     "ar": "وعلى هذا القياس «صلاة الأولى» و«بقلة الحمقاء» متأول بصلاة الساعة الأولى[[٢]]، وبقلة الحبة الحمقاء[[٣]] على الاحتمالين المذكورين،",
     "en": "By the same analogy, “ṣalātu l-ūlā” and “baqlatu l-ḥamqāʾi” are interpreted as “the prayer of the first hour” and “the herb of the foolish seed,” on the two possibilities mentioned."},
    {"type": "matn",
     "ar": "لكن هذا التأويل لا يتمشى في جانب الغربي، فإنه لا شك أن المقصود توصيف الجانب بالغربية لا توصيف مكان هو جانبه بها،",
     "en": "This interpretation, however, does not work for “jānibu l-gharbiyyi,” for there is no doubt that what is intended is to qualify the side as western, not to qualify as western a place of which it is the side;"},
    {"type": "matn",
     "ar": "اللهم إلا أن يقال: هناك مكانان جزء وكل، فالمكان الذي أضيف إليه الجانب هو الجزء، والإضافة بيانية، والمكان الذي اعتبر الجانب بالنسبة إليه هو الكل، فيستقيم المعنى.",
     "en": "unless it be said that there are two places there, a part and a whole: the place to which the side is annexed is the part, the annexation being explicative (bayāniyya), and the place in relation to which the side is considered is the whole; the meaning is then sound."},
    {"type": "matn",
     "ar": "ويرد على القاعدة الثانية: وهي قوله: (و) لا صفة إلى موصوفها (مثل: «جرد قطيفة، وأخلاق ثياب») فإن أصلها: «قطيفة جرد، وثياب أخلاق» قدمت الصفة على الموصوف وأضيف إليه.",
     "en": "Against the second rule—namely his words (and) not an adjective to its qualified noun—there is the objection of (such as “jardu qaṭīfatin” and “akhlāqu thiyābin”), whose origin is “qaṭīfatun jardun” (a worn velvet cloth) and “thiyābun akhlāqun” (threadbare garments); the adjective was put before the qualified noun and annexed to it."},
    {"type": "matn",
     "ar": "وأجيب عنه: بأنه (متأول) بأنهم حذفوا «قطيفة» من قولهم: «قطيفة جرد» حتى صار كأنه اسم غير صفة[[٤]]،",
     "en": "The answer given is that it (is to be interpreted): they elided “qaṭīfa” from their expression “qaṭīfatun jardun” until [jard] became as though it were a noun, not an adjective;"},
    {"type": "matn",
     "ar": "فلما قصدوا تخصيصه، لكونه صالحا لأن يكون قطيفة وغيرها مثل: «خاتم» في كونه صالحا لأن يكون فضة وغيرها أضافوه إلى جنسه الذي يتخصص به كما أضافوا خاتما إلى فضة،",
     "en": "then, when they intended to specify it—since it could be a velvet cloth or something else, like “khātam” (ring), which could be of silver or something else—they annexed it to its genus by which it is specified, just as they annexed “khātam” to “fiḍḍa” (silver);"},
    {"type": "matn",
     "ar": "فليس إضافته إليها من حيث إنه صفة لها، بل من حيث إنه جنس مبهم أضيف إليها ليتخصص، وعلى هذا القياس «أخلاق ثياب».",
     "en": "so its annexation to it is not as an adjective of it, but as an indeterminate genus annexed to it to be specified. “Akhlāqu thiyābin” follows the same analogy."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وحاصله: أن إضافة المسجد إلى الجامع من قبيل إضافة العام إلى الخاص.",
     "en": "Its upshot: the annexation of “al-masjid” to “al-jāmiʿ” is of the kind in which the general is annexed to the particular."},
    {"type": "pair",
     "ar": "وكذا قياس سائر الأمثلة، فتكون تلك الإضافة كإضافة طور سيناء، وصلاة الوتر، وبقلة الكزبرة، وجانب اليمين.",
     "en": "The rest of the examples follow the same analogy, so that annexation is like the annexation in “ṭūru Sīnāʾ” (Mount Sinai), “ṣalātu l-witr” (the witr prayer), “baqlatu l-kuzbara” (the coriander herb) and “jānibu l-yamīn” (the right side)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهي أول ساعة بعد زوال الشمس.",
     "en": "That is the first hour after the sun passes the meridian."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما نسبوها إلى الحمق؛ لأنها تنبت في مجاري السيول ومواطئ الأقدام.",
     "en": "They ascribed foolishness to it only because it grows in torrent beds and where feet tread."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "في أنه يستعمل بدون الموصوف، فإن الصفات لا بد لها من موصوف مذكورا أو مقدرا،",
     "en": "In that it is used without a qualified noun; for adjectives require a qualified noun, stated or supplied;"},
    {"type": "pair",
     "ar": "ووجه صيرورته اسما أنه قصد به ذات الجرد مع قطع النظر عن الوصف، فلم يطلب موصوفا.",
     "en": "and the reason it became a noun is that by it the worn thing itself was intended, disregarding the quality, so it did not call for a qualified noun."},
]
