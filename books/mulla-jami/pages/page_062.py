# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 62 (printed ٦١)."""

PAGE_NUMBER = 62
PRINTED_PAGE = "٦١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "والتخفيف[[١]].",
     "en": "and lightening (takhfīf)."},
    {"type": "matn",
     "ar": "وإنما فسرنا الإضافة بكون الشيء مضافا[[٢]]؛ لأن الفعل أو الجملة[[٣]] قد يقع مضافا إليه[[٤]]، كما في قوله تعالى: ﴿يوم ينفع الصادقين صدقهم﴾[[٥]].",
     "en": "We interpreted “annexation” as the thing’s being the annexed term (muḍāf) [rather than its being that to which annexation is made], because the verb or the sentence may occur as the term annexed to (muḍāf ilayhi), as in His saying, the Exalted: «the Day whereon their truthfulness shall profit the truthful» (Qurʾān, Sūrat al-Māʾida 5:119)."},
    {"type": "matn",
     "ar": "وقد يقال: هذا بتأويل المصدر، أي: يوم نفع الصادقين، فالإضافة بتقدير حرف الجر مطلقا تختص بالاسم.",
     "en": "It may be said: this is by construing [the verb] as a verbal noun, that is, “the day of the profiting of the truthful” (yawma nafʿi al-ṣādiqīn); so annexation by the implicit supposition of the genitive particle, taken unrestrictedly, is peculiar to the noun."},
    {"type": "matn",
     "ar": "وإنما قيدنا الإضافة بقولنا: «بتقدير حرف الجر»، لئلا ينتقض بقولنا: «مررت بزيد»، فإن «مررت» مضاف إلى زيد بواسطة حرف الجر لفظا.",
     "en": "We restricted “annexation” by our saying “by the implicit supposition of the genitive particle” only so that it not be invalidated by our saying “marartu bi-Zaydin” (I passed by Zayd); for “marartu” is annexed to “Zayd” by means of the genitive particle explicitly (in wording)."},

    {"type": "section", "ar": "[ الأسماء المعربة ]",
     "en": "The Declinable Nouns (al-Asmāʾ al-Muʿraba)"},

    {"type": "matn",
     "ar": "(وهو) أي: الاسم قسمان: (معرب)[[٦]] و(مبني)[[٧]]؛ لأنه[[٨]] لا يخلو إما أن يكون مركبا مع غيره، أو لا.",
     "en": "(And it) — that is, the noun — is of two kinds: (declinable, muʿrab) and (indeclinable, mabnī); because it does not escape being either compounded with something else, or not."},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وذلك بحذف التنوين، أو ما يقوم مقامه. ولا يوجد شيء من ذلك في أخويه. وأما الحسن الوجه فمحمول عليه طردا للباب.",
     "en": "That [lightening] is by the elision of the nunation (tanwīn) or of what stands in its place. Nothing of that is found in its two sisters [definiteness and particularization]. As for [an expression like] al-ḥasanu al-wajhi (“the handsome of face”), it is carried upon this [lightening] to keep the category uniform (ṭardan li-l-bāb)."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لا بمعنى ناعت للمضاف والمضاف إليه جميعا. وإنما لم نجعله في مقابلة كون الشيء مضافا إليه؛ إذ لا دليل على تقدير «إليه»، والعطف على الإسناد بعيد، ولقوله قدس سره: «فالإضافة بتقدير حرف الجر مطلقا»،",
     "en": "That is, not in the sense of a term describing both the annexed term (muḍāf) and the annexed-to term (muḍāf ilayhi) together. We did not set it in opposition to “the thing’s being that to which annexation is made,” because there is no evidence for supposing an “ilayhi”; the conjoining [of it] to al-isnād is far-fetched; and [also] on account of his words, may his secret be sanctified: “so annexation by the implicit supposition of the genitive particle, taken unrestrictedly [is peculiar to the noun]”;"},
    {"type": "pair",
     "ar": "ولأن المصنف ردد عبارة المفصل بين هذين الاحتمالين حيث قال: «والإضافة كذلك» يعني: من الخواص إلا أنه لم يرد بها الإضافة مطلقا، فإن أسماء الزمان تضاف إلى الفعل. وإنما أراد المضاف أو أراد الجمع؛ لأنه إنما يضاف إلى الفعل بتأويل المصدر، انتهى.",
     "en": "and because the author alternated the wording of al-Mufaṣṣal between these two possibilities where he said: “and likewise al-iḍāfa” — meaning, [it is] among the [noun’s] properties, except that he did not intend by it annexation unrestrictedly, for the nouns of time are annexed to the verb. Rather he intended [the noun’s being] the annexed term, or he intended the combination [of both]; because [the verb] is annexed only by construal as a verbal noun. End [of the quotation]."},
    {"type": "pair",
     "ar": "إن قلت: كيف يصح إرادة الجميع من الإضافة؟ قلنا: لا شبهة في أنا لا نجد بين المضافين حالة مقيسة تارة إلى طرف، وتارة إلى أخرى، فلعله يدعي أنها يجوز أن تتصور مجردة عن خصوصية الطرفين، وأن لفظة الإضافة موضوعة لها، أو يدعي أن إطلاق الإضافة على قدر مشترك هي مجاز فيه، وحمل الجميع على إرادتها على سبيل البدل بعيد.",
     "en": "If you say: how is it sound to intend “both together” by al-iḍāfa? We say: there is no doubt that between the two annexed terms we find no state analogized (maqīsa) at one time to one side and at another to the other; so perhaps he claims that it can be conceived stripped of the particularity of the two sides, and that the term “iḍāfa” is coined for it, or he claims that the application of “iḍāfa” to a measure shared [between the two] is a metaphorical usage therein; while carrying “both together” upon [the author’s] intending it, by way of substitution (badal), is far-fetched."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أشار إلى اختلاف القولين. ذهب المصنف إلى الأول، وذهب بعضهم إلى الثاني. قال الشيخ الرضي: الظاهر أن المضاف إليه لفظا في نحو: «أتيتك يوم قدم زيد» الجملة الفعلية لا الفعل وحده، كما أن الاسمية في قولك: «أتيتك زمن الحجاج الأمير» هي المضاف إليها. وأما من حيث المعنى فالمصدر هو المضاف إليه الزمان في الجملتين.",
     "en": "He alluded to the disagreement of the two views: the author held the first, and some [others] held the second. Al-Shaykh al-Raḍī said: What is apparent is that the term annexed-to in wording, in an example like “ataytuka yawma qadima Zaydun” (I came to you the day Zayd arrived), is the verbal sentence, not the verb alone — just as the nominal [sentence] in your saying “ataytuka zamana al-Ḥajjāji al-amīri” (I came to you at the time of al-Ḥajjāj the governor) is that which is annexed-to. But from the standpoint of meaning, it is the verbal noun (maṣdar) that is the term to which the time-noun is annexed in the two sentences."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الفعل أو الجملة.",
     "en": "That is, the verb or the sentence."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة المائدة: ١١٩.",
     "en": "Sūrat al-Māʾida: 119."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "من الإعراب بمعنى الإظهار، أو إزالة الفساد، وهو محل إظهار المعاني، وإزالة فساد الالتباس، أو من «أعربت الكلمة» إذا جعلت الإعراب فيها.",
     "en": "[Muʿrab is derived] from iʿrāb in the sense of “making manifest” (iẓhār), or “removing corruption” (izālat al-fasād) — for it [the noun] is the locus of making meanings manifest and of removing the corruption of ambiguity — or from “aʿrabtu al-kalima” (I supplied the word with iʿrāb), when you place the iʿrāb in it."},
    {"type": "pair",
     "ar": "والوجه ظاهر لا من الإعراب العرفي باعتبار أن الإعراب يتحقق فيه؛ لأن القياس معرب -بكسر الراء- كذا في الإيضاح. وفيه أنه لو جاز أخذ صيغة منه لجاز أن يكون اسم مكان لا صفة، حتى يكون القياس ما ذكره.",
     "en": "This derivation is evident, [and it is] not [taken] from iʿrāb in the conventional sense — on the consideration that iʿrāb is realized in it — because [otherwise] the pattern (qiyās) would be muʿrib, with a kasra on the rāʾ [i.e. an active participle, “one that gives iʿrāb”]; thus [it is stated] in al-Īḍāḥ. Against it is that, were it permissible to derive a form from it, it would be permissible for it to be a noun of place rather than an adjective, so that the pattern would be what he mentioned."},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "من البناء المقصود فيه القرار وعدم التغير. وذلك لأنه شبه صوغه في قالب هيئة لا تغير بالبناء.",
     "en": "[Mabnī is] from al-bināʾ, in which are intended fixity and non-alteration; that is because its being cast (ṣawgh) in the mold of a form having no change is likened to building (bināʾ)."},

    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: الاسم.",
     "en": "That is, [the pronoun refers to] the noun."},
]
