# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 400 (printed ٣٩٩)."""

PAGE_NUMBER = 400
PRINTED_PAGE = "٣٩٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لأن كل واحد منهما كلمة واقعة موقع الجملة التي هي من حيث هي لا تستحق» at the foot of PDF p. 399.
    {"type": "matn",
     "ar": "إعرابا ولا بناء[[١]]، فلما وقع المفرد موقعها، ولم يجز خلوه عنهما، رجح البناء الذي هو الأصل في الكلمات قبل التركيب.",
     "en": "…neither inflection (iʿrāb) nor indeclinability (bināʾ); so when a single word occupied its position, and it could not be devoid of both, indeclinability, which is the original state of words before composition, prevailed."},
    {"type": "matn",
     "ar": "ومن الكنايات «كأين»، وإنما بني لأن كاف التشبيه دخلت على «أي»، و«أي» وإن كان في الأصل معربا، لكنه انمحى عن الجزأين معناهما الإفرادي، وصار المجموع كاسم مفرد بمعنى «كم» الخبرية،",
     "en": "Among the allusive nouns (kināyāt) is “kaʾayyin”. It is indeclinable only because the kāf of comparison entered upon “ayy”; and “ayy”, although originally declinable, lost—as did the other part—its meaning as a separate word, and the whole became like a single noun in the sense of predicative “kam” (kam al-khabariyya)."},
    {"type": "matn",
     "ar": "فصار كأنه اسم مبني على السكون آخره نون ساكنة، كما في من لا تنوين تمكن، ولهذا يكتب بعد الياء نون مع أن التنوين لا صورة لها في الخط،",
     "en": "So it became as though it were a noun indeclinable on sukūn whose last letter is a quiescent nūn, as in “man”, not the tanwīn of full declinability (tamakkun); for this reason a nūn is written after the yāʾ, although tanwīn has no form in writing."},
    {"type": "matn",
     "ar": "فمرتبته في البناء منحطة عن أخواتها[[٢]]، فلذلك لم يذكره المصنف معها.",
     "en": "Its rank in indeclinability is therefore lower than that of its sisters, and for this reason the author did not mention it with them."},
    {"type": "matn",
     "ar": "(فـ«كم» الاستفهامية[[٣]]) المتضمنة معنى الاستفهام (مميزها) أي: الذي يرفع الإبهام عن جنس المسؤول عنه (منصوب[[٤]]) على التمييز (مفرد)؛",
     "en": "(So interrogative “kam”), which contains the sense of interrogation: (its specifier (mumayyiz)), that is, what removes the vagueness from the genus of what is asked about, (is accusative), as a specification (tamyīz), (and singular),"},
    {"type": "matn",
     "ar": "لأنها لما كانت للعدد، ووسط العدد وهو من أحد عشر إلى تسعة وتسعين مميزه مفرد منصوب، جعل مميزه كذلك؛ لأنه لو جعل كأحد الطرفين لكان تحكما[[٥]].",
     "en": "because, since it is for number, and the specifier of the middle of number—from eleven to ninety-nine—is singular and accusative, its specifier was made likewise; for had it been made like one of the two extremes, that would have been arbitrary (taḥakkum)."},
    {"type": "matn",
     "ar": "(وكم الخبرية) مميزها (مجرور) بالإضافة (مفرد) تارة (ومجموع) أخرى، تقول:",
     "en": "(And predicative kam): its specifier (is genitive), by annexation, (singular) at one time (and plural) at another. You say:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: «فرع الذي يتحقق معه العامل» printed as is; a noun (e.g. التركيب) seems wanting before «الذي».
    {"type": "pair",
     "ar": "لأن استحقاق الإعراب فرع الذي يتحقق معه العامل، والجملة من حيث هي لا تركيب لها مع غيرها،",
     "en": "Because entitlement to inflection is a consequence of that with which a governor (ʿāmil) is realized, and the sentence as such has no composition with anything else;"},
    {"type": "pair",
     "ar": "واستحقاق البناء فرع لمناسبته بمبني الأصل، ولا مناسبة للجملة مناسبة معتبرة في البناء.",
     "en": "and entitlement to indeclinability is a consequence of its affinity with what is indeclinable by origin, and the sentence has no affinity of the kind that counts for indeclinability."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأنه في الأصل معرب، والكسرة فيه إعراب، والنون تنوين جعل التنوين بمنزلة لام الكلمة، فصار كأنه مبني على السكون، ويحتمل ألا يقول المصنف ببنائه.",
     "en": "Because it is originally declinable: the kasra in it is an inflection, and the nūn is tanwīn, the tanwīn having been treated as the final radical (lām al-kalima), so that it became as though indeclinable on sukūn. It is also possible that the author does not hold that it is indeclinable."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: «كم» الاستفهامية والخبرية يدلان على عدد ومعدود،",
     "en": "That is: interrogative and predicative “kam” both indicate a number and a thing numbered."},
    {"type": "pair",
     "ar": "فالاستفهامية لعدد مبهم عند المتكلم معلوم في ظنه للمخاطب، والخبرية لعدد مبهم عند المخاطب، وربما يعرفه المتكلم.",
     "en": "The interrogative is for a number vague to the speaker and, in his supposition, known to the addressee; the predicative is for a number vague to the addressee, which the speaker may know."},
    {"type": "pair",
     "ar": "وأما المعدود فهو مجهول عند المخاطب فيهما، فلذا احتيج إلى التمييز، ولا يحذف إلا لدليل، والحذف في الاستفهامية أكثر؛ لأنه في صورة الفضلات.",
     "en": "As for the thing numbered, it is unknown to the addressee in both; hence the need for a specification. It is omitted only when there is an indication, and omission is more frequent with the interrogative, because it has the form of the supplementary elements (faḍalāt)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ولا يجوز جره إلا إذا انجرت الاستفهامية بحرف الجر، نحو: «بكم رجل مررت؟» فيجوز أن يكون في تمييزه أيضا الجر قصدا إلى التطابق بينهما.",
     "en": "Its genitive is not permitted except when the interrogative is itself made genitive by a preposition, as in “bi-kam rajulin mararta?” (By how many men did you pass?); then the genitive is also permitted in its specification, aiming at agreement between the two."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: حكما بلا جهة.",
     "en": "That is, a judgement without a ground."},
    {"type": "pair",
     "ar": "فإن قلت: جعله كالوسط أيضا تحكم؟ قلت: الوسط لا يساوي شيئا من الطرفين في كونه طرفا، ويتميز عنهما بكونه وسطا، فلا تحكم.",
     "en": "If you say: making it like the middle is also arbitrary? I say: the middle is not equal to either of the two extremes in being an extreme, and it is distinguished from both by being the middle; so there is no arbitrariness."},
    {"type": "pair",
     "ar": "فلا حاجة في إخراجه عن التحكم إلى ما قاله الفاضل الهندي إنه أكثر، ولا إلى ما ذكره الرضي أن السائل في الأغلب لا يعرف القلة والكثرة، فحملها على الدرجة الوسطى أولى.",
     "en": "So, to remove it from arbitrariness, there is no need for what al-Fāḍil al-Hindī said, that it is the more frequent, nor for what al-Raḍī mentioned: that the questioner mostly does not know whether [the number] is small or large, so referring it to the middle degree is more fitting."},
    {"type": "pair",
     "ar": "والأوجه أن يقال: نصب مميز «كم» الاستفهامية؛ لأنه جعل مميز «كم» الخبرية كالطرفين دفعا للتحكم،",
     "en": "The more cogent view is to say: the specifier of interrogative “kam” is accusative because the specifier of predicative “kam” was made like the two extremes to avoid arbitrariness;"},
    # REVIEW: «تميزا» printed (not «تمييزا»); transcribed as printed. Also «لالتبس بـ«كم» الاستفهامية» is printed; the sense seems to require «الخبرية».
    {"type": "pair",
     "ar": "فلو جعل مميز «كم» الاستفهامية مثلهما، أو مثل أحدهما لالتبس بـ«كم» الاستفهامية، فجعل كالوسط تميزا،",
     "en": "had the specifier of interrogative “kam” been made like them, or like one of them, it would have been confused with interrogative “kam”; so it was made like the middle, for distinction."},
    {"type": "pair",
     "ar": "ولم يعكس؛ لأن «كم» الخبرية متقدمة على الاستفهامية، لكون الاستفهام فرع الخبرية، فجعل كالطرفين؛ لأن الطرف مقدم على الوسط.",
     "en": "It was not reversed, because predicative “kam” precedes the interrogative, since interrogation is derivative of the predicative; so it was made like the two extremes, because the extreme precedes the middle."},
]
