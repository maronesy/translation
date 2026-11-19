# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 499 (printed ٤٩٨)."""

PAGE_NUMBER = 499
PRINTED_PAGE = "٤٩٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وهي بهذا المعنى لا تدخل» at the foot of PDF p. 498 (mid-sentence).
    {"type": "matn",
     "ar": "على اسم صريح، وحمل عليها حتى التي بمعنى «إلى»؛ لأن المعنى الأول أغلب في التي يليها المضارع،",
     "en": "…upon an explicit noun; and the “ḥattā” that means “ilā” was assimilated to it, because the first sense is the more frequent in the [ḥattā] that is followed by the muḍāriʿ."},
    {"type": "matn",
     "ar": "وأما «الواو والفاء وأو» فلأنها لما اقتضت نصب ما بعدها للتنصيص على معنى السببية والجمعية والانتهاء صارت كعوامل النصب، فلم يظهر الناصب بعدها.",
     "en": "As for “the wāw, the fāʾ and aw”: since they require the accusative of what follows them, in order to state explicitly the sense of causation, togetherness and termination, they became like governors of the accusative, so the governor of the accusative does not appear after them."},
    {"type": "matn",
     "ar": "(ويجب) أي: إظهار «أن» (مع «لا») الداخلة على المضارع المنصوب بها (في) صورة دخول (اللام) بمعنى «كي» (عليها) أي: على «أن»",
     "en": "(And it is obligatory), that is, making “an” explicit, (with “lā”) entering upon the muḍāriʿ that is put in the accusative by it, (in) the case of (the lām) in the sense of “kay” entering (upon it), that is, upon “an”;"},
    {"type": "matn",
     "ar": "لاستكراه اللامين المتواليين؛ لام «كي» ولام «لا» نحو قوله تعالى: ﴿لئلا يعلم أهل الكتاب﴾[[١]].",
     "en": "because two consecutive lāms are disliked, the lām of “kay” and the lām of “lā”; as in His words, the Exalted: “So that the People of the Book may know…” (li-allā yaʿlama ahlu al-kitābi)."},
    {"type": "matn",
     "ar": "واعلم أن «أن» الناصبة تضمر في غير المواضع المذكورة كثيرا من غير عمل؛ لضعفها نحو قولهم: «تسمع بالمعيدي خير من أن تراه»،",
     "en": "Know that the “an” that governs the accusative is often left implicit in places other than those mentioned, without governing, owing to its weakness; as in their saying, “tasmaʿu bi-l-Muʿaydiyyi khayrun min an tarāhu” (hearing of al-Muʿaydī is better than seeing him);"},
    {"type": "matn",
     "ar": "ومع عمل مع الشذوذ كقوله:",
     "en": "and [it is left implicit] while governing, though anomalously, as in the poet’s words:"},
    {"type": "verse",
     "ar": "ألا أيهذا اللائمي أحضر الوغى          ...............",
     "en": "Now, you who blame me for being present at the battle … (the second hemistich is not printed)"},
    {"type": "matn",
     "ar": "في رواية النصب، ولكن ليس بقياس كما في تلك المواضع، ولذلك لم يذكرها.",
     "en": "in the reading with the accusative [aḥḍura]; but this is not by regular analogy, as in those places, and for that reason he did not mention them."},

    {"type": "section", "ar": "[جوازم الفعل المضارع]",
     "en": "The Particles that Put the Imperfect Verb in the Jussive"},

    {"type": "matn",
     "ar": "(وينجزم) أي: المضارع (بـ«لم»، و«لما»، و«لام» الأمر، و«لا») المستعملة (في) معنى (النهي) احترازا عما استعمل في معنى النفي،",
     "en": "(And it is put in the jussive), that is, the muḍāriʿ, (by “lam”, “lammā”, the “lām” of command, and “lā”) used (in) the sense of (prohibition), to exclude what is used in the sense of negation;"},
    {"type": "matn",
     "ar": "وهذه الكلمات تجزم فعلا واحدا،",
     "en": "these words put a single verb in the jussive;"},
    {"type": "matn",
     "ar": "(وكلم المجازاة[[٢]]) أي: وينجزم المضارع بكلم المجازاة، أي: كلمات الشرط والجزاء التي بعضها من الأسماء وبعضها من الحروف، ولهذا اختار لفظ الكلم،",
     "en": "(and the words of requital (kalim al-mujāzāt)), that is, the muḍāriʿ is put in the jussive by the words of requital, namely the words of condition and apodosis (sharṭ wa-jazāʾ), some of which are nouns and some particles; for this reason he chose the word “kalim”."},
    {"type": "matn",
     "ar": "والمجزوم بها فعلان",
     "en": "What they put in the jussive is two verbs."},
    {"type": "matn",
     "ar": "(وهي) أي: كلم المجازاة: («إن»، و«مهما»، و«إذما»، و«حيثما») فـ«إذ وحيث» يجزمان المضارع مع «ما»، وأما بدونها فلا.",
     "en": "(They are), that is, the words of requital: (“in”, “mahmā”, “idhmā”, and “ḥaythumā”); “idh” and “ḥaythu” put the muḍāriʿ in the jussive with “mā”, but not without it;"},
    {"type": "matn",
     "ar": "(و«أين»، و«متى») وهما يجزمان المضارع مطلقا سواء كانا مع «ما» أو لا.",
     "en": "(and “ayna” and “matā”), which put the muḍāriʿ in the jussive without restriction, whether with “mā” or not;"},
    {"type": "matn",
     "ar": "(و«ما»، و«من»، و«أي»، و«أنى»).",
     "en": "(and “mā”, “man”, “ayy”, and “annā”)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الحديد: ٢٩.",
     "en": "(Qurʾān, Sūrat al-Ḥadīd 57:29)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: كلمات تدل على كون إحدى الجملتين جزاء للأخرى.",
     "en": "That is, words indicating that one of the two sentences is the requital (jazāʾ) of the other."},
    # REVIEW: printed «الصراخ»; probably a misprint for «الصحاح» (al-Ṣiḥāḥ of al-Jawharī). Transcribed as printed.
    {"type": "pair",
     "ar": "فالمجازاة بمعنى الجزاء على ما في الصراخ جزيته وجازيته بمعنى: اختارها عليه؛ لأن الجزاء يستعمل بمعنى الجملة الجزائية كثيرا.",
     "en": "So “mujāzāt” is in the sense of “jazāʾ”, according to what is in al-Ṣurākh [sic]: “jazaytuhu” and “jāzaytuhu” have the same meaning. He preferred it over it [i.e. jazāʾ], because “jazāʾ” is frequently used in the sense of the apodotic sentence."},
]
