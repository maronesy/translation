# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 192 (printed ١٩١)."""

PAGE_NUMBER = 192
PRINTED_PAGE = "١٩١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "واحترز به عن نحو: «مررت بزيد فإذا له صوت صوت حمار»[[١]]",
     "en": "By this he guarded against such as “I passed by Zayd, and behold, his is a voice, the voice of a donkey” (fa-idhā lahu ṣawtun ṣawta ḥimārin)."},
    {"type": "matn",
     "ar": "(و) على (صاحبه) أي: على صاحب ذلك الاسم، أي: الذي قام به معناه.",
     "en": "(And) [containing] (its possessor—ṣāḥibihi), that is: the possessor of that noun, that is, the one in whom its meaning subsists."},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «مررت بالبلد فإذا به صوت صوت حمار»",
     "en": "By this he guarded against such as “I passed by the town, and behold, in it was a voice, the voice of a donkey.”"},
    # REVIEW: print reads «صوت توصيتا»; the expected maṣdar is «تصويتا»; transcribed as printed.
    {"type": "matn",
     "ar": "(نحو: مررت بزيد فإذا له صوت صوت حمار[[٢]]) أي: يصوت صوت حمار، من «صات[[٣]] الشيء صوتا» بمعنى: صوت توصيتا،",
     "en": "(As in: “I passed by Zayd, and behold, his is a voice, the voice of a donkey”), that is: he voices the voicing of a donkey—from “ṣāta al-shayʾu ṣawtan” (the thing sounded a sound), in the sense of ṣawwata taṣwītan."},
    {"type": "matn",
     "ar": "فـ«صوت حمار» مصدر وقع للتشبيه علاجا بعد جملة، هي قوله: «له صوت»،",
     "en": "So “ṣawta ḥimārin” is a maṣdar occurring for comparison, as a bodily act, after a sentence—namely his words “lahu ṣawtun” (he has a voice)—"},
    {"type": "matn",
     "ar": "وهي مشتملة على اسم بمعنى المفعول المطلق، وهو صوت، ومشتملة على صاحب ذلك الاسم، وهو الضمير المجرور في «له».",
     "en": "which contains a noun in the sense of the absolute object, namely “ṣawt,” and contains the possessor of that noun, namely the genitive pronoun in “lahu.”"},
    {"type": "matn",
     "ar": "(و) نحو: مررت به فإذا له (صراخ صراخ[[٤]] الثكلى) أي: يصرخ صراخ الثكلى، وهي: امرأة مات ولدها.",
     "en": "(And) as in: “I passed by him, and behold, he had (a cry, the cry of the bereaved mother—ṣurākhun ṣurākha al-thuklā),” that is: he cries the crying of the bereaved mother; she is a woman whose child has died."},
    {"type": "matn",
     "ar": "(ومنها) أي: من تلك المواضع (ما وقع) أي: موضع مفعول مطلق وقع (مضمون جملة[[٥]] لا محتمل لها) أي: لهذه الجملة (غيره[[٦]]) أي: غير المفعول المطلق",
     "en": "(And among them)—that is, among those places—is (what occurs), that is, the place of an absolute object that occurs (as the content of a sentence that has no possible [sense]—lā muḥtamala lahā), that is, this sentence, (other than it—ghayruhu), that is, other than the absolute object,"},
    {"type": "matn",
     "ar": "(نحو: له علي ألف درهم[[٧]] اعترافا) أي: «اعترفت اعترافا»[[٨]]، فـ«اعترافا» مصدر وقع مضمون",
     "en": "(as in: “He has a claim on me of a thousand dirhams, by way of acknowledgment”—lahu ʿalayya alfu dirhamin iʿtirāfan), that is: “I acknowledge an acknowledgment.” So “iʿtirāfan” is a maṣdar occurring as the content…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الأولى في مثله الاتباع بأن يكون وصفا أو بدلا. وضعف نصبه؛",
     "en": "Shaykh al-Raḍī said: in its like, concord (itbāʿ) is preferable, its being a qualifier or a substitute. He judged its accusative weak,"},
    {"type": "pair",
     "ar": "لأن الجملة المتقدمة ليست إذن كالفعل لخلوها مما لا بد للفعل منه.",
     "en": "because the preceding sentence is then not like the verb, since it lacks what the verb cannot do without."},
    {"type": "pair",
     "ar": "وقد أجازوا النصب فيه على الحال أو المصدر، لكن لا يجب حذف العامل.",
     "en": "They allowed the accusative in it as a ḥāl or as a maṣdar; but elision of the governor is not obligatory."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جاز انتصابه على أحد تأويلي الوصف، وذو الحال الضمير المستكن في «له».",
     "en": "Its accusative is allowed on one of the two interpretations of the qualifier, the possessor of the ḥāl (dhū al-ḥāl) being the pronoun latent in “lahu.”"},
    {"type": "pair",
     "ar": "وأجاز غير سيبويه رفعه على أنه بدل، أو عطف بيان، أو وصف:",
     "en": "Others than Sībawayh allowed its nominative as a substitute, an explicative apposition, or a qualifier:"},
    {"type": "pair",
     "ar": "وإما على حذف مضاف أي: مثل صوت حمار، كما ذهب إليه الخليل.",
     "en": "either on the elision of an annexed noun, that is: “like the voice of a donkey,” as al-Khalīl held."},
    {"type": "pair",
     "ar": "ويجوز التعريف بأن يقول: صوت الحمار؛ لأن مثلا لا يتعرف بالإضافة.",
     "en": "Definiteness is then allowed, so that one says “ṣawtu al-ḥimār” (the voice of the donkey), because “mithl” does not become definite by annexation."},
    {"type": "pair",
     "ar": "ورد عليه سيبويه بأنه لو جاز هذا لجاز هذا قصير الطويل، أي: مثل الطويل.",
     "en": "Sībawayh objected to him that, were this allowed, “This is a short man, the tall one,” meaning “like the tall one,” would be allowed."},
    {"type": "pair",
     "ar": "وإما على أنه جامد مؤول بالمشتق، أي: منكر فإذا عرف كان بدلا أو عطف بيان لا غير.",
     "en": "Or on its being a non-derived noun interpreted as a derived one, that is, as indefinite; so when it is made definite it is a substitute or an explicative apposition, nothing else."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إلى آخره يعني: أن صوتا جاء مصدرا بمعنى التصويت، فلا حاجة إلى القول بأنه اسم،",
     "en": "[His words “ṣāta…”] to the end: he means that “ṣawt” has come as a maṣdar in the sense of taṣwīt (voicing), so there is no need to say that it is a noun"},
    {"type": "pair",
     "ar": "وأنه استعمل استعمال المصدر كالعطاء بمعنى الإعطاء وأن عامله يصوت من التصويت.",
     "en": "used in the manner of the maṣdar, like ʿaṭāʾ in the sense of iʿṭāʾ (giving), and that its governor is “yuṣawwitu,” from taṣwīt."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قيل: هو اسم استعمل استعمال المصدر.",
     "en": "It has been said: it is a noun used in the manner of the maṣdar."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "حال أو خبر لـ«وقع» على أنه بمعنى «كان». وهذا أظهر معنى.",
     "en": "[Maḍmūna is] a ḥāl, or the predicate of “waqaʿa” taken in the sense of “kāna”; and this is the more evident in meaning."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: print reads «من المصادرة»; probably «من المصادر»; transcribed as printed.
    {"type": "pair",
     "ar": "أي: لا احتمال للجملة من المصادرة غيره، فمحتمل مصدر ميمي وغيره مفعوله.",
     "en": "That is: the sentence has no possible [content] among the maṣdars other than it; so “muḥtamal” is a mīm-maṣdar (maṣdar mīmī), and “ghayruhu” is its object."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "له خبر، و«على» متعلق به، أو بالعكس، ولكل وجه لفظي ومعنوي.",
     "en": "“Lahu” is the predicate and “ʿalā” is attached to it, or the reverse; and each has a verbal and a semantic justification."},
    {"type": "pair",
     "ar": "ومن هذا القبيل قول المجيب: الله أكبر دعوة الحق، أي: دعاء إلى الحق؛ لأنه دعاء إلى الصلاة.",
     "en": "Of this kind is the saying of the one who responds: “Allāhu akbar, the call of truth (daʿwata al-ḥaqq),” that is: a call to the truth; because it is a call to prayer."},
    {"type": "pair",
     "ar": "ومنه أيضا: «إن زيدا لقائم قسما»؛ لأن قسما بمعنى التأكيد، وهو الحاصل في الكلام السابق بسبب «إن» واللام.",
     "en": "Of it also is: “Zayd is indeed standing—an oath” (inna Zaydan la-qāʾimun qasaman); because “qasaman” has the sense of emphasis, and that is what obtains in the preceding utterance through “inna” and the lām."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الجملة المتقدمة في هذا القسم وما يقابله عاملة لتأديتها معنى الفعل.",
     "en": "Shaykh al-Raḍī said: the preceding sentence in this category and its counterpart is [itself] the governor, because it conveys the sense of the verb."},
]
