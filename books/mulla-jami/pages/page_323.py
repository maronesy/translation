# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 323 (printed ٣٢٢)."""

PAGE_NUMBER = 323
PRINTED_PAGE = "٣٢٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(في» at the foot of PDF p. 322 (mid-phrase).
    {"type": "matn",
     "ar": "الأكثر) أي: في أكثر موارد استعمالاته (و«فمي») في بعضها إبقاء للميم المعوض عن الواو عند قطعه عن الإضافة.",
     "en": "…most cases), that is, in most of the occasions of its use, (and “famī”) in some of them, keeping the mīm that substitutes for the wāw when it is cut off from annexation."},
    {"type": "matn",
     "ar": "(وإذا قطعت) هذه الأسماء الخمسة (عن الإضافة قيل: «أخ[[١]] وأب وحم وهن وفم») بالحركات الثلاث[[٢]] (و) لكن (فتح الفاء أفصح منهما) أي: من الضم والكسر.",
     "en": "(When) these five nouns (are cut off from annexation, one says “akh,” “ab,” “ḥam,” “han” and “fam”) with the three vowels; (and) yet (fatḥa on the fāʾ is more eloquent than the two), that is, than ḍamma and kasra."},
    {"type": "matn",
     "ar": "(وجاء «حم»[[٣]] مثل «يد») فيقال: «هذا حم وحمك»، و«رأيت حما وحمك»، و«مررت بحم أو حمك».",
     "en": "(“Ḥam” has also come like “yad”), so one says: “hādhā ḥamun wa-ḥamuki,” “raʾaytu ḥaman wa-ḥamaki,” and “marartu bi-ḥamin aw ḥamiki.”"},
    {"type": "matn",
     "ar": "(و) مثل («خبء») بالهمزة، فيقال: «هذا حمء وحمؤك»، و«رأيت حمأ أو حمأك»، و«مررت بحمء وحمئك».",
     "en": "(And) like (“khabʾ”), with hamza, so one says: “hādhā ḥamʾun wa-ḥamʾuki,” “raʾaytu ḥamʾan aw ḥamʾaki,” and “marartu bi-ḥamʾin wa-ḥamʾiki.”"},
    # REVIEW: print lacks the opening guillemet before «هذا حمو وحموك»; transcribed as printed.
    {"type": "matn",
     "ar": "(و) مثل (دلو) بالواو، فيقال: هذا حمو وحموك»، و«رأيت حموا وحموك»، و«مررت بحمو وحموك».",
     "en": "(And) like (“dalw”), with wāw, so one says: “hādhā ḥamwun wa-ḥamwuki,” “raʾaytu ḥamwan wa-ḥamwaki,” and “marartu bi-ḥamwin wa-ḥamwiki.”"},
    {"type": "matn",
     "ar": "(و) مثل (عصا بالألف) فيقال: «هذا حمى وحماك»، و«رأيت حمى وحماك»، و«مررت بحمى وحماك»",
     "en": "(And) like (“ʿaṣā”, with alif), so one says: “hādhā ḥaman wa-ḥamāki,” “raʾaytu ḥaman wa-ḥamāki,” and “marartu bi-ḥaman wa-ḥamāki,”"},
    {"type": "matn",
     "ar": "(مطلقا) أي: جواز «حم» مثل هذه الأسماء الأربعة مطلقا غير مقيد بحال الإفراد والإضافة، بل تجيء هذه الوجوه فيه في كل من حالتي الإفراد والإضافة.",
     "en": "(without restriction), that is, “ḥam” may be like these four nouns without restriction, not limited to the state of standing alone or of annexation; rather, these forms occur in it in each of the two states, standing alone and annexed."},
    {"type": "matn",
     "ar": "(وجاء «هن» مثل «يد» مطلقا) أي: في الإفراد والإضافة، يقال: «هذا هن، ورأيت هنا، ومررت بهن»، و«هذا هنك، ورأيت هنك، ومررت بهنك».",
     "en": "(“Han” has come like “yad” without restriction), that is, standing alone and annexed: one says “hādhā hanun, raʾaytu hanan, marartu bi-hanin,” and “hādhā hanuka, raʾaytu hanaka, marartu bi-hanika.”"},
    {"type": "matn",
     "ar": "(و«ذو»[[٤]] لا يضاف إلى مضمر)؛ لأنه وضع وصلة[[٥]] إلى الوصف بأسماء الأجناس،",
     "en": "(And “dhū” is not annexed to a pronoun), because it was coined as a means of reaching description by generic nouns (asmāʾ al-ajnās),…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا بحث عن غير المضاف ذكر تقريبا،",
     "en": "This is a discussion of the non-annexed [noun], mentioned by way of association (taqrīban)."},
    # REVIEW: print reads «أدني» (with dotted yāʾ) where «أدنى» is expected; transcribed as printed.
    {"type": "pair",
     "ar": "ويقال ترتيب اللغات في الفصاحة هكذا دلو وعصا ويد وخبء، ولغة أدني منها هي كسواء.",
     "en": "It is said that the order of the dialectal forms in eloquence is thus: [like] dalw, ʿaṣā, yad and khabʾ; and a form lower than these is like sawāʾ."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لكن بمتابعة الحركات الإعرابية، وضمير أفصح منهما عائد إلى غير المذكور لتعين المرجح في مقام ترجيح الفتح.",
     "en": "But following the case vowels. The pronoun in “afṣaḥ minhumā” refers to something not mentioned, since the referent is determined in the context of preferring the fatḥa."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لم يراع في الذكر درجات فصاحة اللغات، وإلا فالحق أن يقول: كدلو وعصا ويد وخبء،",
     "en": "In the listing he did not observe the degrees of eloquence of the forms; otherwise he should rightly have said: like dalw, ʿaṣā, yad and khabʾ."},
    {"type": "pair",
     "ar": "وفيه لغة سادسة أدنى الكل، وهي أن يكون كوشاء.",
     "en": "It has a sixth form, the lowest of all, namely that it be like washāʾ."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "اعلم أن عينه واو ولامه ياء.",
     "en": "Know that its middle radical (ʿayn) is wāw and its final radical (lām) is yāʾ."},
    {"type": "pair",
     "ar": "أما الأول فلأن مؤنثة ذات. وأصلها ذوات كنوات بدليل أن مثناها ذواتا حذف عينها لكثرة الاستعمال.",
     "en": "The first, because its feminine is dhāt, whose original form is dhawāt, like nawāt, as shown by its dual dhawātā; its ʿayn was elided through frequency of use."},
    {"type": "pair",
     "ar": "وأما الثاني فلأن باب الطي أغلب من باب القوة، والحمل على الأغلب أولى،",
     "en": "The second, because the class of ṭayy (roots with medial wāw and final yāʾ) is more frequent than the class of quwwa (with wāw in both), and assigning to the more frequent is preferable."},
    {"type": "pair",
     "ar": "ووزنه فلس عند الفراء. والمشهور أن وزنه فوس؛ إذ لو كان كفلس لقلب في المؤنث واوه ياء كطية،",
     "en": "Its pattern is [that of] fals according to al-Farrāʾ. The well-known view is that its pattern is [that of] faras; for were it like fals, its wāw would have turned into yāʾ in the feminine, as in ṭayya."},
    {"type": "pair",
     "ar": "ولا يدل أذواء جمع ذو على أنه مفتوح العين.",
     "en": "And “adhwāʾ,” the plural of dhū, does not show that its ʿayn has fatḥa."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: إنهم إذا أرادوا أن يصفوا شخصا بالذهب مثلا لم يتأت لهم أن يقولوا: جاءني رجل ذهب فجاؤوا بذو، فأضافوه إليه فقالوا: ذو ذهب.",
     "en": "Shaykh al-Raḍī said: when they wished to describe a person by gold, for example, they could not say “a man gold came to me,” so they brought “dhū” and annexed it to it, saying “dhū dhahab” (possessor of gold)."},
    {"type": "pair",
     "ar": "ولما كان جنس المضمرات والأعلام مما لا يقع صفة لم يتوصل بذو إلى الوصف بهما وإن كان بعد التوصل يصير الوصف هو المضاف دون المضاف",
     "en": "Since the genus of pronouns and proper names is among what does not serve as an attribute, “dhū” was not used to reach description by them, even though after this means is used the attribute becomes the annexed noun, not the annexed…"},
]
