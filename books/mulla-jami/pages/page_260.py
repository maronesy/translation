# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 260 (printed ٢٥٩)."""

PAGE_NUMBER = 260
PRINTED_PAGE = "٢٥٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(أطيب منه» from the foot of PDF p. 259.
    {"type": "matn",
     "ar": "رطبا) وهو ما فيه حلاوة صرفة،",
     "en": "…as ruṭab [ripe dates]”)—ruṭab being [dates] in which there is pure sweetness."},
    {"type": "matn",
     "ar": "فهما مع كونهما جامدين حالان، لدلالتهما على صفة البسرية والرطبية،",
     "en": "Though both are underived, they are ḥāls, because they denote the quality of being busr and of being ruṭab;"},
    {"type": "matn",
     "ar": "ولا حاجة إلى أن يؤول البسر بـ«المبسر»[[١]] والرطب بـ«المرطب» من «أبسر النخل»: إذا صار ما عليه بسرا، و«أرطب» إذا صار ما عليه رطبا.",
     "en": "and there is no need to construe busr as mubsir and ruṭab as murṭib, from “absara al-nakhl,” said when what is on [the palm] has become busr, and “arṭaba,” when what is on it has become ruṭab."},
    {"type": "matn",
     "ar": "والعامل في «رطبا» «أطيب» باتفاق النحاة، وفي «بسرا» أيضا عند محققيهم،",
     "en": "The governor of “ruṭaban” is “aṭyab” by agreement of the grammarians, and of “busran” too according to their verifying scholars;"},
    {"type": "matn",
     "ar": "وتقدم «بسرا» على اسم التفضيل مع ضعفه في العمل؛ لأنه إذا تعلق بشيء واحد حالان باعتبارين مختلفين يلزم أن يلي كل منهما متعلقه،",
     "en": "and “busran” precedes the elative despite its weakness in governing, because when two ḥāls attach to one thing under two different considerations, each must follow what it attaches to."},
    {"type": "matn",
     "ar": "والبسرية تعلقت بالمشار إليه بـ«هذا» من حيث إنه مفضل،",
     "en": "Being busr attaches to what is pointed to by “hādhā” insofar as it is the thing preferred;"},
    {"type": "matn",
     "ar": "وهذه الحيثية وإن لم تكن معتبرة فيه إلا بعد إضماره في «أطيب»، لكنه لما كان الضمير بالنسبة إلى المظهر كالعدم[[٢]] أقيم المظهر مقامه، وأوجبوا أن يليه،",
     "en": "and although this respect is considered in it only after it is made a concealed pronoun in “aṭyab,” yet since the pronoun is as nothing relative to the overt noun, the overt noun was put in its place, and they required [the ḥāl] to follow it."},
    {"type": "matn",
     "ar": "والرطبية تعلقت به من حيث إنه مفضل عليه، وهو ضمير «منه»، فيجب أن يليه.",
     "en": "Being ruṭab attaches to it insofar as it is that over which preference is given, namely the pronoun of “minhu,” so it must follow that."},
    {"type": "matn",
     "ar": "قال الرضي: «وأما الضمير المستكن في أفعل»، فإنه وإن كان مفضلا لكنه لما لم يظهر كان كالعدم،",
     "en": "Al-Raḍī said: “As for the pronoun concealed in afʿal, although it is the thing preferred, since it is not overt it is as nothing.”"},
    {"type": "matn",
     "ar": "ومع هذا فلا أرى بأسا بأن يقال وإن لم يسمع: «زيد أحسن قائما منه قاعدا».",
     "en": "Even so, I see no harm in saying, though it is not attested: “Zayd is finer standing than he is sitting.”"},
    {"type": "matn",
     "ar": "وذهب بعضهم: إلى أن العامل في «بسرا» اسم الإشارة أي: أشير إليه حال كونه بسرا،",
     "en": "Some held that the governor of “busran” is the demonstrative, that is: “I point to it while it is busr.”"},
    {"type": "matn",
     "ar": "وهذا ليس بصحيح؛ لأنه يمكن أن يكون المشار إليه التمر اليابس، فلا تتقيد الإشارة بحالة البسرية[[٣]]،",
     "en": "This is not correct, because what is pointed to may be dry dates, so the pointing is not restricted to the state of being busr;"},
    {"type": "matn",
     "ar": "ولأنه يصح حيث وقع موقع اسم الإشارة اسم لا يصح إعماله فيه نحو: «تمرة نخلي بسرا أطيب منه رطبا»[[٤]].",
     "en": "and because [the construction] is correct where in place of the demonstrative there stands a noun that cannot govern it, as in “The fruit of my palm as busr is better than it as ruṭab.”"},
    {"type": "matn",
     "ar": "(وتكون) أي: الحال (جملة[[٥]]) لدلالتها على الهيئة كالمفردات، فيصح أن وقعت حالا مثلها،",
     "en": "(And it may be)—that is, the ḥāl—(a clause), because it denotes a state as single words do, so it may properly occur as a ḥāl like them;"},
    {"type": "matn",
     "ar": "ولكن يجب أن تكون الجملة الحالية (خبرية) محتملة للصدق والكذب؛",
     "en": "but the circumstantial clause must be (declarative [khabariyya]), admitting truth and falsehood;…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا إذا كان هذا إشارة إلى النخل؛ لأن المبسر هو النخل كما يدل عليه اشتقاقه.",
     "en": "This is when “hādhā” points to the palm, since the mubsir is the palm, as its derivation shows."},
    {"type": "pair",
     "ar": "وأما إذا كان إشارة إلى التمر كما هو الظاهر، فتأويلها بالنضج وغير النضج أو المدرك وغير المدرك.",
     "en": "But if it points to the dates, as is apparent, then they are construed as “ripe” and “unripe,” or “mature” and “immature.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الأظهر لما كان المستتر بالنسبة إلى المظهر والبارز كالعدم، فافهم.",
     "en": "It would be clearer [to say]: “since the concealed pronoun is as nothing relative to the overt noun and the visible pronoun”; so understand."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه أنه فليكن حينئذ حالا مقدرة.",
     "en": "Against this: then let it be an anticipated ḥāl."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يقال: هذا المثال مصنوع لا يوثق به.",
     "en": "It is said: this example is contrived and not to be relied upon."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: قد تقام الجملة الحالية مقام مفرد، فيعرب الجزء الأول منهما إعراب الحال، ويلزم تنكيره لقيامه مقام الحال،",
     "en": "Shaykh al-Raḍī said: a circumstantial clause is sometimes put in place of a single word; its first part then takes the inflection of the ḥāl and must be indefinite, since it stands in the place of the ḥāl;"},
    {"type": "pair",
     "ar": "وفاه إلى في شاذ، نحو يدا بيد أي: ذو يد بذي يد أي: النقد بالنقد،",
     "en": "and “fāhu ilā fiyya” is anomalous. Examples are “hand to hand” (yadan bi-yadin), that is, one with a hand [giving] to one with a hand, that is, cash for cash;"},
    {"type": "pair",
     "ar": "ونحو: بعت الشاء بشاة بدرهم، والأصل كل شاة بدرهم، وكذا قولهم: بعت الشاء شاة ودرهما.",
     "en": "and “I sold the sheep, a sheep for a dirham,” the base being “each sheep for a dirham”; and likewise their saying “I sold the sheep, a sheep and a dirham.”"},
    {"type": "pair",
     "ar": "والواو بمعنى مع كما في «كل رجل وضيعته» أي: شاة ودرهم مقرونان، فنصب ههنا الجزآن لقبولهما الإعراب.",
     "en": "The wāw means “with,” as in “every man and his estate,” that is, a sheep and a dirham coupled together; here both parts are in the accusative because both can take inflection."},
    {"type": "pair",
     "ar": "قال الخليل: يجوز أن يأتي به على الأصل نحو: بعت الشاء شاة بدرهم وشاة ودرهم.",
     "en": "Al-Khalīl said: one may say it in its base form, as in “I sold the sheep, a sheep for a dirham” and “a sheep and a dirham.”"},
]
