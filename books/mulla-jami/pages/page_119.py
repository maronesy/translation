# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 119 (printed ١١٨)."""

PAGE_NUMBER = 119
PRINTED_PAGE = "١١٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "و«بذر»[[١]] لماء، و«خضم»[[٢]] لرجل، أفعال نقلت إلى الاسمية.",
     "en": "And «Badhdhara» — [a name] for a [particular] water — and «Khaḍḍama» — [a name] for a man: these are verbs that have been transferred to nominal usage."},
    {"type": "matn",
     "ar": "وأما نحو: «بقم» اسما لصيغ معروف، وهو العندم، و«شلم»[[٣]] علما لموضع بالشام، فهو من الأسماء العجمية المنقولة إلى العربية، فلا يقدح في ذلك الاختصاص.",
     "en": "As for the like of «Baqqama» — a name for a well-known dye, namely dragon’s blood (al-ʿandam) — and «Shallama», a proper name for a place in Syria (al-Shām): it belongs to the non-Arabic (ʿajamī) nouns transferred into Arabic, so that does not impair this [verbal] specificity (ikhtiṣāṣ)."},
    {"type": "matn",
     "ar": "(و) مثل: (ضرب) على البناء للمفعول[[٤]] إذا جعل علما لشخص، فإنه أيضا غير منصرف للعلمية ووزن الفعل.",
     "en": "(And) the like of (ḍuriba), in the passive construction (al-bināʾ li-l-mafʿūl), when it is made a proper name for a person, is likewise imperfectly inflected (a diptote), on account of proper-nounhood (ʿalamiyya) and the verbal pattern (wazn al-fiʿl)."},
    {"type": "matn",
     "ar": "وإنما قيدنا بالبناء للمفعول، فإنه على البناء للفاعل غير مختص بالفعل[[٥]]، ولم يذهب إلى منع صرفه إلا بعض النحاة[[٦]].",
     "en": "We restricted it to the passive construction only because, in the active construction (al-bināʾ li-l-fāʿil), it is not peculiar to the verb; and none but some grammarians held [the view of] denying it full inflection."},
    {"type": "matn",
     "ar": "٢-(أو يكون[[٧]]) غير مختص، لكن يكون (في أوله) أي: في أول وزن الفعل[[٨]]، أو أول ما كان على وزن الفعل (زيادة) أي: زيادة حرف، أو حرف زائد[[٩]] من حروف",
     "en": "2 – (Or it may be) not peculiar [to the verb], yet there is (at its beginning) — that is, at the beginning of the verbal pattern, or of whatever is upon the verbal pattern — (an augmentation): namely, the augmentation of a letter, or an augmented letter, from the letters of"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "من بذر المال، أي: أسرف.",
     "en": "From “badhdhara al-māl,” that is: he squandered [wealth]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "من خضم الشيء أكله بجميع فمه.",
     "en": "From “khaḍama al-shayʾ”: he ate it with his whole mouth."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "مرتجلا بالعبرانية لموضع بالشام، يقال: هو بيت المقدس.",
     "en": "[It is] a name coined extemporaneously (murtajal) in Hebrew for a place in Syria; it is said to be Jerusalem (Bayt al-Maqdis)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وزن فعل مجهولا من الخواص لم يأت في أسماء الأجناس إلا دئل لدويبة.",
     "en": "The passive verbal pattern (fuʿila) is among the peculiarities [of the verb]; it has not occurred among generic nouns except in “duʾil,” [the name] of a small creature."},
    {"type": "pair",
     "ar": "وقيل: العرب قد تنقل الفعل إلى أسماء الأجناس وإن كان قليلا، كقوله عليه الصلاة والسلام: «إن الله تعالى ينهاكم عن قيل وقال».",
     "en": "It has [also] been said: the Arabs may transfer the verb to generic nouns, even if [this is] rare, as in his statement — may Allah bless him and grant him peace — “Allah, the Exalted, forbids you idle chatter (qīl wa-qāl).”"},
    {"type": "pair",
     "ar": "فيجوز أن يكون منقولا من دئل بمعنى أسرع.",
     "en": "So it may be [that “duʾil” is] transferred from “duʾila” in the sense of “he hastened.”"},
    {"type": "pair",
     "ar": "وأما دئل علما لقبيلة، فيجوز أن يكون منقولا منه، ومن دأل بمعنى مشى مشيا مخصوصا، والتغيير للدلالة على العلمية كما قيل في شمس شمس بالضم.",
     "en": "As for “Duʾil” as a proper name of a tribe, it may be transferred from it [i.e., the verb], and from “daʾala” in the sense of walking in a particular manner, the alteration [of the vowelling] being to signal proper-nounhood — as was said regarding “Shams” [the verb] versus “Shums” with a ḍamma."},
    {"type": "pair",
     "ar": "وأما الوعل لغة في الوعل، والرئم بمعنى الاست فشاذان.",
     "en": "As for “al-wuʿil” — a dialectal variant of “al-waʿl” (mountain goat) — and “al-riʾm” in the sense of the posterior, these two are anomalous (shādhdhān)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بخلاف بناء المجهول، فإنه لم يجيء في الأسماء إلا ألفاظ قليلة ملحقة بالعدم، كحكم وسلم ورجب.",
     "en": "Unlike the passive construction, for it has occurred among nouns only in a few words that are treated as negligible (mulḥaqa bi-l-ʿadam), such as Ḥukam, Sulam, and Rajab."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "هذا لا يصلح وجها للتقييد بالبناء للمفعول. وإنما قال: يوجه به شرط الاختصاص بالفعل أو الزيادة.",
     "en": "This does not serve as a ground for restricting [the discussion] to the passive construction. Rather he said: what is warranted thereby is the condition of specificity to the verb, or the augmentation."},
    {"type": "pair",
     "ar": "وذلك البعض يونس، فإن الوزن المشترك عنده سبب مطلقا، وعيسى بن عمر النحوي، فإنه ذهب إلى أن الوزن المشترك يؤثر بشرط نقل اللفظ من الفعل إلى الاسم.",
     "en": "That “some [grammarians]” are Yūnus — for the shared pattern is, in his view, a cause absolutely — and ʿĪsā ibn ʿUmar the grammarian, for he held that the shared pattern is operative on condition that the word be transferred from the verb to the noun."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "إنما لم يقل بدله: «أو يغلب» كما قاله النحاة؛ لأن فاعلا إذا جعل علما لمذكر كان منصرفا مع أنه غالب في الأفعال.",
     "en": "He did not say in its place “or it predominates,” as the grammarians say, only because a word of the pattern fāʿil, when made a proper name for a masculine, is fully inflected, even though [fāʿil] predominates in verbs."},
    {"type": "pair",
     "ar": "ولم يجيء في الأسماء إلا حاتم وعالم وساسم اسم شجر أسود، ولأن في إثبات الغلبة زيادة مؤنة، لايقال في إثبات الاختصاص أيضا تلك الزيادة؛ لأنا نقول: لعله لم يجد فيه ما يحترز به عن ذلك المحذور.",
     "en": "And it has occurred among nouns only in Ḥātim, ʿĀlim, and Sāsim — the name of a black tree; and because establishing predominance involves an added burden. Let it not be said that establishing specificity likewise involves that added [burden]; for we say: perhaps he found in it nothing by which to guard against that objectionable [consequence]."},
    {"type": "pair",
     "ar": "إن قلت: هذا الوزن إنما يصح سببا إذا كان له زيادة اختصاص بالفعل، حتى يظهر فرعيته، وزيادة الاختصاص إما بالاختصاص بالفعل أو بالغلبة؟",
     "en": "If you say: this pattern is valid as a cause only if it has an added specificity to the verb, so that its derivative status becomes manifest; and added specificity is either through [outright] exclusivity to the verb or through predominance [— so which is it]?"},
    {"type": "pair",
     "ar": "قلنا: زيادة تلك الحروف قياسية في جميع الأفعال المتصرفة، فصارت لاطرادها في جميع الأفعال دون الأسماء أشد اختصاصا بالفعل.",
     "en": "We say: the augmentation of those letters is regular (qiyāsī) in all the conjugable verbs, so that, by its consistent occurrence throughout all the verbs but not the nouns, it came to have a stronger specificity to the verb."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لما كان المراد من وزن الفعل: كون الاسم على وزن الفعل صح رجع الضمير إلى الوزن وإلى الموزون كما هو المقصود.",
     "en": "Since what is meant by “the verbal pattern” is that the noun be upon the pattern of the verb, it is valid for the pronoun to refer back both to the pattern (al-wazn) and to that which is patterned (al-mawzūn), as is intended."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "على الأول صح لفظة «في»؛ لأن الصفة تنسب إلى موصوفها بـ«في»، وهو شائع.",
     "en": "On the first [reading] the word “fī” (in) is sound, because an attribute is related to that which it qualifies by means of “fī,” and this is common."},
    {"type": "pair",
     "ar": "وكذا على الثاني؛ لأن النسبة بين قوله: أوله وبين الحرف الزائد العموم من وجه، ويصح نسبة العام إلى الخاص بـ«في» وبالعكس، أو لأن المراد في موضع أوله.",
     "en": "And likewise on the second [reading], because the relation between his phrase “its beginning” and “the augmented letter” is one of overlap (ʿumūm min wajh); and it is valid to relate the general to the particular by means of “fī,” and vice versa; or because what is meant is “in the position of its beginning.”"},
]
