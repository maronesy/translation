# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 408 (printed ٤٠٧)."""

PAGE_NUMBER = 408
PRINTED_PAGE = "٤٠٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «فلا فرق بين ما أعرب من هذه الظروف المقطوعة وبين ما بني منها.» at the foot of PDF p. 407 (new sentence).
    {"type": "matn",
     "ar": "وقال بعضهم: بل إنما أعربت لعدم تضمنها معنى الإضافة، فمعنى كنت قبلا أي: قديما.",
     "en": "Some said: rather, they are declined only because they do not contain the meaning of annexation; so the meaning of “kuntu qablan” is “formerly”."},
    {"type": "matn",
     "ar": "وقال الشارح الرضي: «والأول هو الحق».",
     "en": "The commentator al-Raḍī said: “The first is the truth.”"},
    {"type": "matn",
     "ar": "(وأجري مجراه) أي: مجرى الظرف المقطوع عن الإضافة («لا غير» و«ليس غير»[[١]]) في حذف المضاف إليه، والبناء على الضم",
     "en": "(And treated like it), that is, like the adverb cut off from annexation, (are “lā ghayru” and “laysa ghayru”), in the omission of the annexed noun and in being indeclinable with ḍamma,"},
    {"type": "matn",
     "ar": "وإن لم يكن «غير» من الظروف لشبهه بالغايات، لشدة الإبهام الذي فيه كما فيها،",
     "en": "even though “ghayr” is not one of the adverbs, because it resembles the ghāyāt (end-points) through the intense vagueness in it, as in them."},
    {"type": "matn",
     "ar": "ولا يحذف منه المضاف إليه إلا بعد «لا وليس» نحو: «افعل هذا لا غير، وجاءني زيد ليس غير» لكثرة استعمال «غير» بعدهما",
     "en": "Its annexed noun is omitted only after “lā” and “laysa”, as in “ifʿal hādhā lā ghayru” (do this, nothing else) and “jāʾanī Zaydun laysa ghayru” (Zayd came to me, no one else), because of the frequent use of “ghayr” after them."},
    {"type": "matn",
     "ar": "(و) كذلك أجري مجرى الظروف («حسب») لشبهها بـ«غير» في كثرة الاستعمال، وعدم تعرفها بالإضافة[[٢]].",
     "en": "(And) likewise (“ḥasbu”) is treated like the adverbs, because it resembles “ghayr” in frequency of use and in not becoming definite through annexation."},
    {"type": "matn",
     "ar": "(ومنها) أي: من الظروف المبنية («حيث») للمكان. وقال الأخفش: وقد يستعمل للزمان",
     "en": "(And among them), that is, among the indeclinable adverbs, is (“ḥaythu”) (where), for place. Al-Akhfash said: it is sometimes used for time."},
    {"type": "matn",
     "ar": "(ولا يضاف إلا إلى جملة) اسمية كانت أو فعلية (في الأكثر) أي: في أكثر الاستعمالات، وقد جاء:",
     "en": "(It is annexed only to a sentence), whether nominal or verbal, (in most cases), that is, in most usages. There has occurred:"},
    {"type": "verse",
     "ar": "أما ترى حيث سهيل طالعا          ……………",
     "en": "Do you not see where Suhayl is rising …"},
    {"type": "matn",
     "ar": "فـ«حيث» فيه مضاف إلى مفرد، وهو «سهيل» مفعول «ترى» أي: «أما ترى مكان سهيل طالعا» آخره:",
     "en": "Here “ḥaythu” is annexed to a single word, namely “Suhayl”, [and it is] the object of “tarā”, that is, “do you not see the place of Suhayl rising”. Its ending is:"},
    {"type": "verse",
     "ar": "……………          نجم يضيء كالشهاب ساطعا",
     "en": "… a star that shines like a blazing meteor, gleaming."},
    {"type": "matn",
     "ar": "وإنما بنيت على الضم كالغايات؛ لأنها غالبة الإضافة إلى الجملة، والمضاف إلى الجملة في الحقيقة مضاف إلى المصدر الذي تضمنته الجملة،",
     "en": "It is indeclinable with ḍamma, like the ghāyāt, only because it is predominantly annexed to a sentence; and what is annexed to a sentence is in reality annexed to the maṣdar contained in the sentence."},
    {"type": "matn",
     "ar": "فهي وإن كانت في الظاهر مضافة الجملة، فإضافتها إليها كلا إضافة، فشابهت الغايات المحذوف ما أضيفت إليه، فبنيت على الضم مثلها،",
     "en": "So although it is outwardly annexed to the sentence, its annexation to it is like no annexation; it thus resembles the ghāyāt whose annexed noun is omitted, and so it is indeclinable with ḍamma like them."},
    # REVIEW: «مضافة الجملة» printed as such (one might expect «مضافة إلى الجملة»); transcribed as printed.
    {"type": "matn",
     "ar": "ومع الإضافة إلى المفرد يعربه بعضهم، لزوال علة البناء أي: الإضافة إلى الجملة، والأشهر بقاؤه على بنائه لشذوذ الإضافة إلى المفرد.",
     "en": "When it is annexed to a single word, some decline it, because the cause of indeclinability, namely annexation to a sentence, has gone; but the better-known view is that it remains indeclinable, because annexation to a single word is anomalous."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وغير خبر «ليس» أي: ليس الجائي غيره. وقال الأخفش: يجوز أن يكون اسمه، كذا في الرضي.",
     "en": "“Ghayr” is the predicate of “laysa”, that is, “the one who came is not other than he”. Al-Akhfash said: it may be its subject; so in al-Raḍī."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأعجب أن يقال: لأن «حسب» بمعنى «لا غير»؛ إذ لا فرق بين أن يقال: «جاء زيد فحسب» وبين أن يقال: «جاء زيد لا غير»،",
     "en": "It would be more pleasing to say: because “ḥasb” is in the sense of “lā ghayr”, since there is no difference between saying “jāʾa Zaydun fa-ḥasbu” (Zayd came, and that is all) and saying “jāʾa Zaydun lā ghayru” (Zayd came, no one else)."},
    {"type": "pair",
     "ar": "والغفلة عن هذا الوجه أعجب، وليت شعري أنه لم لم يجعل حسب مناسبا للغايات في الإبهام؛ لأنه لإبهامه لا يتعرف كـ«غير».",
     "en": "Overlooking this reason is more surprising still; I wish I knew why he did not make “ḥasb” akin to the ghāyāt in vagueness, since, because of its vagueness, it does not become definite, like “ghayr”."},
]
