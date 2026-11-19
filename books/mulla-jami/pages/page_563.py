# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 563 (printed ٥٦٢)."""

PAGE_NUMBER = 563
PRINTED_PAGE = "٥٦٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(و) دخول اللام (في «لكن») على اسمها، أو خبرها، أو على ما بينهما (ضعيف)؛",
     "en": "(And) the entry of the lām (with “lākinna”), upon its noun, its predicate or what lies between them, (is weak),"},
    {"type": "matn",
     "ar": "لأنها وإن لم تغير معنى الجملة، لكن لا توافق اللام مثل «إن» في معناه الذي هو التأكيد.",
     "en": "because, although it does not alter the meaning of the sentence, it does not agree with the lām, as “inna” does, in its meaning, which is emphasis."},
    {"type": "matn",
     "ar": "وقد جاء مع ضعفه في قول الشاعر:",
     "en": "Despite its weakness it has occurred in the poet’s words:"},
    {"type": "verse",
     "ar": "....................          ولكنني من حبها لعميد",
     "en": "…… but I am, from love of her, indeed heart-stricken."},
    {"type": "matn",
     "ar": "(وتخفف) «إن» (المكسورة) لثقل التشديد وكثرة الاستعمال (فيلزمها) بعد التخفيف (اللام، وحينئذ يجوز إلغاؤها) أي: إبطال عملها، وهو الغالب؛",
     "en": "(And) “inna” (with kasra may be lightened), because of the heaviness of the doubled consonant and the frequency of use; (then) after lightening (the lām is required with it, and in that case its cancellation is permitted), that is, voiding its government, and this is the predominant usage,"},
    {"type": "matn",
     "ar": "لفوات بعض وجوه مشابهتها مع الفعل، كفتح الآخر، وكونها على ثلاثة أحرف،",
     "en": "because some aspects of its resemblance to the verb are lost, such as the fatḥa on its final letter and its consisting of three letters;"},
    {"type": "matn",
     "ar": "كما يجوز إعمالها على ما هو الأصل، ولهذا لم يذكره صريحا، واللام على كلا التقديرين لازم لها.",
     "en": "just as giving it government is permitted, as is the original state; this is why he did not mention it explicitly. On both construals the lām is required with it:"},
    {"type": "matn",
     "ar": "أما في الإلغاء، فللفرق بين المخففة والنافية في مثل: «إن زيد قائم» و«إن زيد لقائم».",
     "en": "in cancellation, to distinguish the lightened form from the negating [in], as in “in Zaydun qāʾimun (Zayd is not standing)” and “in Zaydun la-qāʾimun (Zayd is indeed standing)”;"},
    {"type": "matn",
     "ar": "وأما في الإعمال، فلطرد الباب، ولأن كثيرا من الأسماء لا يظهر فيه إعراب لفظي؛ لكون إعرابه تقديريا، أو لكونه مبنيا.",
     "en": "and in government, for consistency of the category, and because many nouns show no inflection in wording, their inflection being implicit (taqdīrī) or their being indeclinable."},
    {"type": "matn",
     "ar": "وهذا خلاف مذهب سيبويه وسائر النحاة، فإنهم قالوا: عند الإعمال «لا يلزمها اللام؛ لحصول الفرق بالعمل».",
     "en": "This is contrary to the doctrine of Sībawayh and the rest of the grammarians, for they said that when it governs, “the lām is not required with it, since the distinction is achieved by the government”."},
    {"type": "matn",
     "ar": "(ويجوز دخولها) أي: دخول «إن» المخففة (على فعل من أفعال المبتدأ) أي: من الأفعال[[١]] التي هي من دواخل المبتدأ والخبر لا غير، مثل: «كان، وظن»، وأخواتهما،",
     "en": "(And its entry is permitted), that is, the entry of lightened “in”, (upon a verb among the verbs of the subject), that is, among the verbs that enter upon the subject and predicate and no others, such as “kāna” and “ẓanna” and their sisters,"},
    {"type": "matn",
     "ar": "لأن الأصل دخولها عليهما، فإذا فات ذلك اشترط ألا يفوت دخولها على ما يقتضي المبتدأ والخبر، رعاية للأصل بحسب الإمكان،",
     "en": "because its original use is to enter upon the two [subject and predicate]; so when that is lost, it was made a condition that its entry upon what requires a subject and predicate not be lost, so as to preserve the original as far as possible,"},
    {"type": "matn",
     "ar": "كقوله تعالى: ﴿وإن كانت لكبيرة﴾[[٢]]، ﴿وإن نظنك لمن الكاذبين﴾[[٣]].",
     "en": "as in His words, the Exalted: “and it was indeed a great thing” and “and we indeed think you are one of the liars”."},
    {"type": "matn",
     "ar": "(خلافا للكوفيين في التعميم) أي: تعميم الدخول وعدم تخصيصه بدواخل المبتدأ والخبر، لا في أصل الدخول على الفعل، فإنه متفق عليه.",
     "en": "(In disagreement with the Kūfans regarding generalization), that is, generalizing its entry and not restricting it to the verbs that enter upon subject and predicate; not regarding entry upon the verb as such, which is agreed upon."},
    {"type": "matn",
     "ar": "فالكوفيون خالفوا البصريين في تجويز دخولها على غير دواخلهما متمسكين بقول الشاعر:",
     "en": "So the Kūfans disagreed with the Baṣrans in permitting its entry upon verbs other than those that enter upon them, relying on the poet’s words:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فالإضافة في المتن لأدنى ملابسة، وهي أفعال القلوب، والأفعال الناقصة وأفعال المقاربة.",
     "en": "So the genitive construction in the matn is for the slightest connection; these are the verbs of the heart (afʿāl al-qulūb), the incomplete verbs (al-afʿāl al-nāqiṣa) and the verbs of proximity (afʿāl al-muqāraba)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة البقرة: ١٤٣.",
     "en": "Qurʾān, Sūrat al-Baqara 2:143."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الشعراء: ١٨٦.",
     "en": "Qurʾān, Sūrat al-Shuʿarāʾ 26:186."},
]
