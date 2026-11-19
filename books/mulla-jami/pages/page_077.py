# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 77 (printed ٧٦)."""

PAGE_NUMBER = 77
PRINTED_PAGE = "٧٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn + sharḥ) ----------------
    {"type": "matn",
     "ar": "٣-(مضافة[[١]])؛ لأنها[[٢]] إذا كانت مكبرة، وموحدة، ولم تكن مضافة أصلا، فإعرابها بالحركات، نحو: «جاءني أخ»، و«رأيت أخا»، و«مررت بأخ».",
     "en": "3. (annexed [muḍāfa]) — because, when they are augmentative, singular, and not annexed at all, their declension is by vowels, as in: “a brother came to me” (jāʾanī akhun), “I saw a brother” (raʾaytu akhan), and “I passed by a brother” (marartu bi-akhin)."},
    {"type": "matn",
     "ar": "٤-فينبغي أن تكون مضافة، ولكن (إلى غير ياء المتكلم[[٣]])؛ لأنها إذا كانت مضافة إلى ياء المتكلم، فحالها كسائر الأسماء المضافة إليها.",
     "en": "4. So they ought to be annexed, but (to other than the first-person yāʾ [ilā ghayri yāʾ al-mutakallim]) — because, when they are annexed to the first-person yāʾ, their state is like that of the rest of the nouns annexed to it [i.e., declined by estimated vowels]."},
    {"type": "matn",
     "ar": "ولم يكتف في هذا الشرط بالمثال[[٤]]، لئلا يتوهم اشتراط إضافتها بكونها[[٥]] إلى الكاف.",
     "en": "He did not content himself, for this condition, with the [mere] example, lest it be imagined that the requirement of their annexation is that it be [specifically] to the [pronominal] kāf."},
    {"type": "matn",
     "ar": "وإنما جعل إعراب هذه الأسماء بالحروف؛ لأنهم[[٦]] لما جعلوا إعراب المثنى، وجمع المذكر السالم بالحروف، أرادوا أن يجعلوا إعراب بعض الآحاد أيضا كذلك،",
     "en": "The declension of these nouns was made to be by letters only because, when they [the grammarians] made the declension of the dual and the sound masculine plural by letters, they wished to make the declension of some of the singulars likewise,"},
    {"type": "matn",
     "ar": "لئلا يكون بينهما[[٧]] وبين الآحاد[[٨]] وحشة ومنافرة تامة.",
     "en": "so that there should not be, between the two [the dual and the plural] and the singulars, complete estrangement and disharmony."},
    {"type": "matn",
     "ar": "وإنما اختاروا أسماء ستة؛ لأن إعراب كل من المثنى والمجموع ثلاثة، فجعلوا[[٩]] في مقابلة كل إعراب اسما،",
     "en": "They chose [precisely] six nouns only because the declension of each of the dual and the plural is threefold, so they set, corresponding to each [type of] declension, one noun,"},
    {"type": "matn",
     "ar": "وإنما اختاروا هذه الأسماء الستة[[١٠]]، لمشابهتها المثنى[[١١]]",
     "en": "and they chose these six nouns in particular because of their resemblance to the dual"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه تغيير لنظم المتن حيث أخر قوله: «مضافة» عن قوله «بالواو» إلى آخره. وذلك إما لأنه جعل قوله «مضافة» حالا من المستتر في الظرف، وجعل الظرف عاملا فيه، وحينئذ تكون العبارة محمولة على التقديم والتأخير، وإلا فالحال لا يتقدم على العامل المعنوي، فلذا قدم ما أخره،",
     "en": "In this there is an alteration of the arrangement of the matn, since he deferred his word “muḍāfa” (annexed) from his words “bi-l-wāw” to the end. This is either because he made his word “muḍāfa” a circumstantial qualifier (ḥāl) of the pronoun latent in the adverbial phrase (ẓarf), taking the ẓarf as its governor — in which case the expression is to be construed as [a case of] fronting and postponing (taqdīm wa-taʾkhīr), for otherwise a ḥāl cannot precede its abstract governor, and so he brought forward what he had [logically] deferred;"},
    {"type": "pair",
     "ar": "أو لأن للمزاج تغيير النظم لنكتة كالعناية، أو حسن الموقع، أو موافقة الأسلوب السابق إلى غير ذلك. ولا يخفى أن قوله: «مضافة» يجوز أن يكون حالا من معمول الإعراب المفهوم من المقام أو المقدر في نظم الكلام.",
     "en": "or because the disposition [of good style] may alter the arrangement for some subtlety, such as [special] attention, felicity of position, or conformity to the preceding style, and so on. It is not hidden that his word “muḍāfa” may [also] be a ḥāl of the object of the iʿrāb understood from the context or implied in the arrangement of the discourse."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لأن الأسماء.",
     "en": "That is: because the [six] nouns [are so]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: إلى الياء.",
     "en": "That is: [annexed] to the [first-person] yāʾ."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "تفصيله: أن خصوصية المضاف إليه المذكور غير معتبرة، والقصد إلى نفي الإضافة إلى ياء المتكلم فقط، وهو غاية في الخفاء، فاحتيج إلى التصريح به،",
     "en": "Its detailed explanation: the particularity of the mentioned term of annexation (al-muḍāf ilayhi) is not intended; the aim is solely to negate annexation to the first-person yāʾ, which is exceedingly subtle, so explicit statement of it was needed;"},
    {"type": "pair",
     "ar": "وليس الاحتراز عن المصغر بصيغة المكبر، ولا عن المثنى والمجموع بصيغة الواحد كذلك.",
     "en": "and it is not [a matter of] guarding against the diminutive by means of the augmentative form, nor against the dual and plural by means of the singular form — likewise [these are already clear from the examples]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: الإضافة.",
     "en": "That is: the annexation."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: النحاة أو العرب.",
     "en": "That is: the grammarians, or the Arabs."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: بين المثنى والجمع المذكر.",
     "en": "That is: between the dual and the masculine plural."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ولأن الحروف وإن كانت فروعا للحركات في باب الإعراب لثقلها وخفة الحركات إلا أنها أقوى؛ لأن كل حرف من تلك الحروف كحركتين أو أكثر، فكرهوا أن يستند المثنى والمجموع مع كونهما فرعين للمفرد بالإعراب الأقوى.",
     "en": "And because the letters, though they are subsidiary (furūʿ) to the vowels in the domain of declension — on account of their heaviness and the lightness of the vowels — are nonetheless stronger, since each of those letters is equivalent to two vowels or more; so they were averse that the dual and the plural should rely upon the stronger declension, while they are themselves branches of the singular."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: فوضعوها.",
     "en": "That is: so they instituted them."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "لا يخفى أن هذا الوجه في غاية الضعف، والأقرب منه أن يقال: المعرب بالحروف في الفرع والملحق به ستة: المثنى، وكلا، واثنان، والجمع، وأولو، وعشرون، فجعلوا في مقابلة كل فرع أصلا.",
     "en": "It is not hidden that this line of reasoning is exceedingly weak. Closer [to correctness] than it is to say: those declined by letters, among the branch-forms and what is annexed to them, are six: the dual, kilā, ithnān (two), the [sound] plural, ūlū, and ʿishrūn (the twenties); so they set, corresponding to each branch-form, an original (aṣl)."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "في كون معانيها منبئة عن تعدد كالأخ دون غد ليظهر ذلك التعدد، وخصوا ذلك بحال الإضافة.",
     "en": "[Their resemblance lies] in the fact that their meanings connote plurality — like akh (brother), as opposed to ghad (tomorrow) — so that this plurality may become manifest; and they restricted that to the state of annexation."},
]
