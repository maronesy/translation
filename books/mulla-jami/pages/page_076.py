# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 76 (printed ٧٥)."""

PAGE_NUMBER = 76
PRINTED_PAGE = "٧٥"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section",
     "ar": "[ المعرب الحروف ]",
     "en": "That Which Is Declined by Letters"},

    # ---------------- Main text (matn + sharḥ) ----------------
    {"type": "matn",
     "ar": "(أخوك، وأبوك، وحموك) بكسر الكاف؛ لأن الحم قريب المرأة من جانب زوجها، فلا يضاف إلا إليها.",
     "en": "(akhūka [your brother], wa-abūka [and your father], wa-ḥamūki [and your father-in-law]) — with a kasra on the kāf, because the ḥam (in-law) is a relative of the woman from the side of her husband, so it is annexed only to her."},
    {"type": "matn",
     "ar": "(وهنوك) والهن: الشيء المنكر الذي يستهجن ذكره[[١]]، كالعورة والصفات الذميمة، والأفعال القبيحة.",
     "en": "(wa-hanūka) — the han is the disapproved thing whose mention is deemed unseemly, such as the pudenda, blameworthy attributes, and vile deeds."},
    {"type": "matn",
     "ar": "وهذه الأسماء الأربعة منقوصات واوية.",
     "en": "These four nouns are curtailed ones (manqūṣāt) with an original wāw."},
    {"type": "matn",
     "ar": "(وفوك) وهو أجوف واوي، لامه هاء؛ إذ أصله فوه[[٢]].",
     "en": "(wa-fūka [your mouth]) — it is a hollow noun with a medial wāw, its lām being a hāʾ, since its origin is fawah."},
    {"type": "matn",
     "ar": "(وذو مال) وهو لفيف مقرون بالواوين؛ إذ أصله ذوو،",
     "en": "(wa-dhū mālin [possessor of wealth]) — it is a “paired defective” (lafīf maqrūn) with two wāws, since its origin is dhawaw;"},
    {"type": "matn",
     "ar": "وإنما أضيف (ذو) إلى الاسم الظاهر دون الكاف؛ لأنه[[٣]] لا يضاف إلا إلى أسماء الأجناس[[٤]].",
     "en": "and dhū is annexed only to an explicit noun and not to the [pronominal] kāf, because it is annexed only to generic nouns (asmāʾ al-ajnās)."},
    {"type": "matn",
     "ar": "فإعراب هذه الأسماء الستة[[٥]] (بالواو) رفعا[[٦]]، (والألف) نصبا، (والياء) جرا، ولكن لا مطلقا: بل حال كونها:",
     "en": "The declension (iʿrāb) of these six nouns is (with the wāw) in the nominative, (with the alif) in the accusative, and (with the yāʾ) in the genitive — but not absolutely; rather [only] when they are:"},
    {"type": "matn",
     "ar": "١- مكبرة، إذ مصغرها[[٧]] بالحركات[[٨]] معربة، نحو: «جاءني أخيك»، و«رأيت أخيك»، و«مررت بأخيك».",
     "en": "1. in their augmentative (non-diminutive) form — for their diminutive is declined by vowels — as in: “your little brother came to me” (jāʾanī ukhayyuka), “I saw your little brother” (raʾaytu ukhayyaka), and “I passed by your little brother” (marartu bi-ukhayyika)."},
    {"type": "matn",
     "ar": "٢- وموحدة؛ إذ المثنى والمجموع منها معرب بإعراب التثنية والجمع.",
     "en": "2. and in their singular form — for their dual and plural are declined with the declension of the dual and the plural."},
    {"type": "matn",
     "ar": "وإنما لم يصرح[[٩]] بهذين القيدين اكتفاء بالأمثلة.",
     "en": "He (the author) refrained from stating these two conditions explicitly, contenting himself with the examples."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "من الرجل والمرأة.",
     "en": "[Namely, deemed unseemly] by both the man and the woman."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "حذفت الهاء لمجرد التخفيف، ثم تقلب الواو ياء إذا أضيف إلى ياء المتكلم، فيقال: في، وقد يستعمل بالميم أيضا فيقال: فمي. وإذا أضيف إلى غير ياء المتكلم فيرد الميم إلى الواو، فيتلفظ بها حال الرفع، وتقلب الواو ألفا حال النصب، وياء حال الجر.",
     "en": "The hāʾ was elided merely for lightening; then the wāw is turned into a yāʾ when it is annexed to the first-person yāʾ, so one says fiyya; and it is also sometimes used with the mīm, so one says famī. When it is annexed to other than the first-person yāʾ, the mīm is reverted to the wāw, so it is pronounced [as wāw] in the nominative, the wāw turning into an alif in the accusative and a yāʾ in the genitive."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: ذو.",
     "en": "That is: dhū."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كالمال والعلم.",
     "en": "Such as “wealth” (al-māl) and “knowledge” (al-ʿilm)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لا بخصوصها، بل بعمومها؛ إذ كثيرا ما يجري حكم على شخص، ويراد به الحكم على نوعه، فحاصله: أن الأسماء الستة حكمها كذا.",
     "en": "That is: not with respect to their specific [wording], but with respect to their generality — for often a ruling is applied to an individual while what is intended is the ruling upon its kind; so its upshot is: that the ruling of the six nouns is such-and-such."},
    {"type": "pair",
     "ar": "قيل في توجيه تلك الإرادة أن اللفظ إذا أريد به مجرد اللفظ يكون علما، والعلم يصح تأويله بالصفة المشتهر مسماه بها، فيصح أن يؤول أبوك إلى آخره بالصفة التي اشتهرت بها، وهي كونها أسماء ستة، وفيه ما مر من تزييف كون اللفظ موضوعا لنفسه.",
     "en": "It has been said, in explaining that intent, that the wording — if by it merely the wording is meant — becomes a proper name, and a proper name may be construed by way of the well-known attribute by which its bearer is named; so it is valid that “abūka,” and so on, be construed by the attribute by which it became famous, namely its being [called] “six nouns” — though therein lies what was mentioned before regarding the unsoundness of a wording’s being posited for itself."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا بالحركة التقديرية أو اللفظية، وهي حركة ما قبل حروف المد، كما قيل؛ للزوم الإعراب في الوسط والعدول إلى خلاف الأصل، وهو التقدير مع الغناء عنه.",
     "en": "Not by an estimated or a pronounced vowel — that is, the vowel preceding the letters of prolongation — as has been said [by some]; for that would entail placing the declension medially and departing from the norm, namely resorting to estimation (taqdīr) when one can dispense with it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: ما يصغر منها. وإنما قلنا ذلك؛ لأن (ذو) لا يصغر.",
     "en": "That is: those of them [that admit diminution and so take vowels]; and we said this only because dhū is not diminutized."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لأنه يتحرك عينه ولامه وجوبا ليتم وزن فعيل، وحرف العلة المجعول إعرابا يجب سكونه ليشابه الحركة.",
     "en": "Because its ʿayn and lām are necessarily vowelled so that the pattern fuʿayl may be completed, whereas the weak letter that is made an inflectional marker must be quiescent so as to resemble a vowel."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "المصنف.",
     "en": "[Namely,] the author."},
]
