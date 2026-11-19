# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 222 (printed ٢٢١)."""

PAGE_NUMBER = 222
PRINTED_PAGE = "٢٢١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "والمندوب في اللغة: «ميت يبكى عليه أحد، ويعد محاسنه؛ ليعلم الناس أن موته أمر عظيم؛ ليعذروه في البكاء ويشاركوه في التفجع».",
     "en": "Lexically, the mandūb is “a dead person over whom someone weeps and whose virtues he recounts, so that people may know that his death is a grave matter, excuse him in his weeping and share with him in the lamentation (tafajjuʿ).”"},
    {"type": "matn",
     "ar": "وفي الاصطلاح: (هو المتفجع عليه[[١]]) وجودا أو عدما (بـ«يا» أو «وا»[[٢]])",
     "en": "Technically, (it is the one lamented over), whether in its existence or its non-existence, (with “yā” or “wā”)."},
    {"type": "matn",
     "ar": "فالمتفجع عليه عدما ما يتفجع على عدمه، كالميت الذي يبكى عليه النادب،",
     "en": "What is lamented over in its non-existence is that whose absence is lamented, like the dead person over whom the mourner weeps;"},
    {"type": "matn",
     "ar": "والمتفجع عليه وجودا ما يتفجع على وجوده عند فقد المتفجع عليه عدما كالمصيبة والحسرة والويل اللاحقة للنادب لفقد الميت،",
     "en": "what is lamented over in its existence is that whose presence is lamented upon the loss of what is lamented over in its non-existence, such as the calamity, the grief and the woe that befall the mourner through the loss of the dead person."},
    {"type": "matn",
     "ar": "فالحد شامل لقسمي المندوب مثل: «يا زيداه ويا عمراه»، ومثل: «يا حسرتاه، ويا مصيبتاه، ويا ويلاه».",
     "en": "So the definition covers both kinds of mandūb, as in “yā Zaydāh, yā ʿAmrāh,” and as in “yā ḥasratāh (O my grief), yā muṣībatāh (O my calamity), yā waylāh (O my woe).”"},
    {"type": "matn",
     "ar": "(واختص) المندوب (بـ«وا») ممتازا به[[٣]] عن المنادى، لعدم دخوله عليه، بخلاف «يا»، فإنه مشترك بينهما.",
     "en": "(And) the mandūb (is specific to “wā”), being distinguished by it from the vocative, since it does not enter upon the vocative; unlike “yā,” which is shared between them."},
    {"type": "matn",
     "ar": "(وحكمه) أي: حكم المندوب (في الإعراب والبناء حكم المنادى) أي: مثل حكمه،",
     "en": "(And its rule), that is, the rule of the mandūb, (in declension and indeclinability is the rule of the vocative), that is, like its rule;"},
    {"type": "matn",
     "ar": "يعني: إذا وقع المندوب على صورة قسم من أقسام المنادى، فحكمه في الإعراب والبناء مثل حكم ذلك القسم من المنادى،",
     "en": "he means: when the mandūb takes the form of one of the kinds of vocative, its rule in declension and indeclinability is like the rule of that kind of vocative;"},
    {"type": "matn",
     "ar": "كما إذا كان مفردا معرفة يضم، وإذا كان مضافا أو مشابها به ينصب،",
     "en": "thus when it is single and definite it takes the ḍamma, and when it is annexed or resembles the annexed it takes the accusative."},
    # REVIEW: print reads «ليرد» (= li-yarida); transcribed as printed.
    {"type": "matn",
     "ar": "ولا يلزم من ذلك جواز وقوعه على صورة جميع أقسام المنادى ليرد أنه لا يقع نكرة[[٤]]؛ لأنه لا يندب إلا المعرفة.",
     "en": "It does not follow from this that it may take the form of every kind of vocative, so that the objection would arise that it does not occur indefinite; for only a definite noun is lamented."},
    {"type": "matn",
     "ar": "(و) جاز (لك زيادة الألف[[٥]] في آخره) أي: آخر المندوب[[٦]] لمد الصوت المطلوب في الندبة",
     "en": "(And) it is permitted (to you to add an alif at its end), that is, at the end of the mandūb, to prolong the voice, as is sought in lamentation (nudba)."},
    {"type": "matn",
     "ar": "(فإن خفت اللبس[[٧]]) أي: التباس ذلك اللفظ عند زيادة الألف بغيره عدلت",
     "en": "(If you fear confusion), that is, that the word, once the alif is added, will be confused with another, you turn…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "صلته اللام، فالظاهر المتفجع له.",
     "en": "Its proper complement is the lām, so the obvious [wording] would be “al-mutafajjaʿ lahu.”"},
    {"type": "pair",
     "ar": "ولعل على بمعنى لام الأجل كما يقال في المحمود عليه، أو لتضمن معنى البكاء.",
     "en": "Perhaps “ʿalā” has the sense of the lām of cause, as is said in “al-maḥmūd ʿalayhi,” or it is because [the verb] includes the sense of weeping."},
    {"type": "pair",
     "ar": "وفيه أنه لا يشمل المتفجع عليه وجودا.",
     "en": "There is the objection that it does not cover what is lamented over in its existence."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الباء للإلصاق صفة للمتفجع عليه، وليست للسببية أو الاستعانة.",
     "en": "The bāʾ is of attachment (ilṣāq), [forming] a qualifier of “the one lamented over”; it is not of causation or of instrument."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أشار به إلى أن الباء متعلق بالاختصاص لتضمنه معنى الامتياز.",
     "en": "By this he indicated that the bāʾ is attached to “ikhtaṣṣa” because it includes the sense of being distinguished."},
    {"type": "pair",
     "ar": "ودخول الباء في المقصور أعرب من دخوله في المقصور عليه.",
     "en": "The bāʾ entering upon what is restricted is more proper Arabic than its entering upon that to which it is restricted."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: note reads «إلا المعروف» where the matn has «إلا المعرفة»; transcribed as printed.
    {"type": "pair",
     "ar": "ليس ورود هذا باعثا قويا على تأويل قوله: وحكمه في الإعراب والبناء حكم المنادى بما أوله به",
     "en": "The occurrence of this [objection] is no strong motive for interpreting his words “and its rule in declension and indeclinability is the rule of the vocative” in the way he interpreted them,"},
    {"type": "pair",
     "ar": "لكون قوله: ولا يندب إلا المعروف في حكم المستثنى عن قوله: وحكمه في الإعراب والبناء حكم المنادى.",
     "en": "since his words “only the known (al-maʿrūf) is lamented” stand as an exception to his words “and its rule in declension and indeclinability is the rule of the vocative.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الأندلسي: إذا كان المندوب مع «يا» يجب زيادة الألف لئلا يلتبس بالمنادى.",
     "en": "Al-Andalusī said: when the mandūb is with “yā,” the addition of the alif is obligatory, so that it is not confused with the vocative."},
    {"type": "pair",
     "ar": "وقال الرضي: إن كانت قرينة تدل على الندبة لا يجب زيادة الألف مع ياء أيضا، وإلا فيجب.",
     "en": "Al-Raḍī said: if there is a contextual indication pointing to lamentation, the addition of the alif is not obligatory even with yāʾ; otherwise it is obligatory."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وقد يلحق في آخر غير المندوب.",
     "en": "It is sometimes attached to the end of what is not a mandūb."},

    # ---------------- Footnote 7 (continues on p.223) ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: المتحرك بالحركات الإعرابية لا يلحقه إلا الألف، ويقدر الإعراب نحو: وا ضرب الرجلا في المسمى بضرب الرجل،",
     "en": "Shaykh al-Raḍī said: to what bears declensional vowels only the alif is attached, and the declension is implied, as in “wā Ḍaraba al-rajulā” for one named Ḍaraba al-rajul;"},
    {"type": "pair",
     "ar": "وكذا المتحرك بالحركات البنائية إلا عند اللبس، والمصنف يتبعها",
     "en": "likewise what bears indeclinable vowels, except when there is confusion; and the author makes it follow…"},
]
