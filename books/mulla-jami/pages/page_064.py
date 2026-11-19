# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 64 (printed ٦٣)."""

PAGE_NUMBER = 64
PRINTED_PAGE = "٦٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "٢- والأمر بغير اللام.",
     "en": "2 — the imperative verb, [formed] without the [prefixed] lām [of command]."},

    {"type": "matn",
     "ar": "٣- والحرف.",
     "en": "3 — the particle (ḥarf)."},

    {"type": "matn",
     "ar": "وبهذا القيد خرج مثل: «هؤلاء» في مثل: «قام هؤلاء»، لكونه[[١]] مشابها لمبني الأصل، كما سيجيء في بابه[[٢]] إن شاء الله تعالى.",
     "en": "By this restriction there is excluded the likes of “hāʾulāʾi” in expressions such as “qāma hāʾulāʾi,” since it resembles that which is indeclinable in origin, as will come in its chapter, Allah the Exalted willing."},

    {"type": "matn",
     "ar": "اعلم أن «صاحب الكشاف» جعل الأسماء المعدودة العارية عن المشابهة المذكورة معربة.",
     "en": "Know that the author of al-Kashshāf [al-Zamakhsharī] deemed the enumerated nouns that are devoid of the aforementioned resemblance to be declinable (muʿrab)."},

    {"type": "matn",
     "ar": "وليس النزاع في المعرب الذي هو اسم مفعول من قولك: «أعربت»، فإن ذلك لا يحصل إلا بإجراء الإعراب على آخر الكلمة بعد التركيب، بل في المعرب اصطلاحا، فاعتبر العلامة[[٣]] مجرد الصلاحية، لاستحقاق الإعراب بعد التركيب، وهو الظاهر[[٤]] من كلام الإمام عبد القاهر.",
     "en": "The dispute is not about “muʿrab” in the sense of the passive participle derived from your saying “aʿrabtu” (I inflected [it]) — for that is realized only by applying inflection to the end of the word after composition — but rather about “muʿrab” in its technical sense. So al-ʿAllāma [al-Zamakhsharī] took into account merely the fitness (ṣalāḥiyya) for deserving inflection after composition; and this is what is apparent from the words of al-Imām ʿAbd al-Qāhir [al-Jurjānī]."},

    {"type": "matn",
     "ar": "واعتبر المصنف مع وجود الصلاحية حصول الاستحقاق بالفعل[[٥]]، ولهذا أخذ «التركيب»[[٦]] في تعريفه.",
     "en": "The author, however, required — together with the presence of fitness — the actual attainment of deservingness (istiḥqāq bi-l-fiʿl); and for this reason he included “composition” (al-tarkīb) in his definition."},

    {"type": "matn",
     "ar": "وأما وجود الإعراب بالفعل في كون الاسم معربا، فلم يعتبره أحد.",
     "en": "As for the actual presence of inflection being [required] for a noun’s being declinable, no one has taken it into account."},

    {"type": "matn",
     "ar": "وإنما عدل المصنف عما هو المشهور عند الجمهور[[٧]] من أن المعرب: ما اختلف آخره باختلاف العوامل؛ لأن الغرض من تدوين علم النحو[[٨]] أن يعرف به[[٩]] أحوال أواخر الكلم في التركيب من لم يتتبع لغة العرب، ولم",
     "en": "The author departed from what is well-known among the majority — namely that the muʿrab is that whose ending varies with the variation of the governing agents (ʿawāmil) — only because the purpose of compiling the science of grammar (naḥw) is that one who has not [directly] traced the speech of the Arabs may come to know through it the states of the endings of words in composition, and has not…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: لكون هؤلاء فيه.",
     "en": "That is: because of “hāʾulāʾi” being in it [the example]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: باب المبني. فيه أن صاحب الكافية لم يبين في باب المبني مناسبة كل مبني لمبني الأصل من أي جهة، كما يفهم من هذا الكلام.",
     "en": "That is: the chapter on the indeclinable (al-mabnī). [A remark] upon it: the author of al-Kāfiya did not clarify, in the chapter on the indeclinable, the respect in which every indeclinable corresponds to what is indeclinable in origin, as is understood from this statement."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: أن العلامة اكتفى في تحقق المعرب بكونه قابلا لوجود أسباب الإعراب فيه سواء وجدت ك«زيد» في «قام زيد»، أو لم توجد ك«زيد».",
     "en": "He means: al-ʿAllāma was content, for the realization of muʿrab, with its being receptive to the presence of the causes of inflection in it — whether they are present, as with “Zayd” in “qāma Zaydun,” or not present, as with “[isolated] Zayd.”"},
    {"type": "pair",
     "ar": "والمصنف لم يكتف به، بل زاد مع القابلية وجود الأسباب التي بها يستحق الاسم لأن يعطى الإعراب وهي التركيب، وتحقق العامل معه، وعدم المشابهة لمبني الأصل.",
     "en": "The author, however, was not content with that, but added — alongside receptivity — the presence of the causes by which the noun deserves that inflection be assigned to it: namely composition, the realization of the governing agent along with it, and the absence of resemblance to what is indeclinable in origin."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: ما اعتبره العلامة.",
     "en": "That is: what al-ʿAllāma took into account."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا حاجة هنا إلى ذكر الصلاحية؛ إذ الاستحقاق بالفعل لا يتحقق بدون صلاحية الاستحقاق.",
     "en": "There is no need here to mention fitness, since actual deservingness cannot be realized without the fitness for deservingness."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إذ به يحصل الاستحقاق بالفعل. والحاصل أن العلامة اعتبر الإعراب بالقوة البعيدة من الفعل، والمصنف اعتبر الإعراب بالقوة القريبة من الفعل.",
     "en": "For by it [composition] actual deservingness is attained. The upshot is that al-ʿAllāma took inflection into account by remote potentiality (al-quwwa al-baʿīda) relative to actuality, whereas the author took it into account by proximate potentiality (al-quwwa al-qarība) to actuality."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "كأنهم وقعوا في ذلك من لفظ المعرب، ووجود الإعراب في أفراده، فتوهموا أن حقيقته العرفية ذلك، ولم يعرفوا أن ذلك من عوارضه المفارقة.",
     "en": "It is as though they fell into that [view] on account of the word “muʿrab” and the presence of inflection in its instances, so they supposed that its conventional reality was that; they did not realize that this is one of its separable accidents (ʿawāriḍ mufāriqa)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "اعلم أن الغرض من النحو لا يقتصر عليه كما يدل عليه هذا الكلام، بل الغرض منه معرفة الهيئات التركيبية، وتقديم ما حقه التقديم، وتأخير ما حقه التأخير.",
     "en": "Know that the purpose of grammar is not confined to this, as this statement implies; rather, its purpose [also includes] knowing the compositional forms, giving precedence to what deserves precedence, and postponing what deserves postponement."},
    {"type": "pair",
     "ar": "مثلا وجوب تقديم المتضمن بمعنى الاستفهام على سائر أجزاء الكلام مما يتعلق بعلم النحو، فالأولى أن يقول: من جملة الغرض من علم النحو إلى آخره.",
     "en": "For example, the obligation of fronting that which carries the sense of interrogation ahead of the remaining parts of speech — of what pertains to the science of grammar. So it would be more fitting for him to say “among the purposes of the science of grammar…,” and so forth."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: بعلم النحو.",
     "en": "That is: by the science of grammar."},
]
