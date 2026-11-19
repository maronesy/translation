# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 385 (printed ٣٨٤)."""

PAGE_NUMBER = 385
PRINTED_PAGE = "٣٨٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(ومن ثمة) أي: ومن أجل أنه إذا تعذر أمر منها تعذر الإخبار (امتنع) الإخبار» at the foot of PDF p. 384.
    {"type": "matn",
     "ar": "بالذي (في ضمير الشأن[[١]]) بأن يكون ضمير الشأن مخبرا عنه لامتناع تصدير الجملة بالذي، وتأخير المخبر عنه خبرا؛ لوجوب تقديمه على الجملة.",
     "en": "…by means of alladhī (in the case of the pronoun of the matter) (ḍamīr al-shaʾn), that is, by making the pronoun of the matter the thing reported about; because it is impossible to begin the sentence with alladhī and to put the thing reported about at the end as the predicate, since [that pronoun] must precede the sentence."},
    {"type": "matn",
     "ar": "(و)كذلك امتنع في (الموصوف) بدون الصفة (وفي الصفة[[٢]]) بدون الموصوف،",
     "en": "(And) likewise it is impossible in the case of (the qualified noun) (mawṣūf) without its qualifier, (and in the case of the qualifier) (ṣifa) without the qualified noun."},
    {"type": "matn",
     "ar": "فلا يجوز في «ضربت زيدا العاقل» أن يخبر بـ«الذي» عن «زيد» بدون العاقل، ولا عن «عاقل» بدون زيد لاستلزامه وقوع الضمير صفة أو موصوفا،",
     "en": "So in “ḍarabtu Zaydan al-ʿāqila” (I struck Zayd the intelligent) one may not report by means of “alladhī” about “Zayd” without “al-ʿāqil”, nor about “ʿāqil” without “Zayd”, because that entails the pronoun’s occurring as a qualifier or a qualified noun;"},
    {"type": "matn",
     "ar": "بخلاف ما إذا أخبرت عن مجموعهما، فيقال: «الذي ضربته زيد العاقل».",
     "en": "unlike when you report about the two together, for then one says: “alladhī ḍarabtuhu Zaydun al-ʿāqilu” (the one whom I struck is Zayd the intelligent)."},
    {"type": "matn",
     "ar": "(و) كذلك امتنع في (المصدر العامل[[٣]]) بدون المعمول،",
     "en": "(And) likewise it is impossible in the case of (the governing verbal noun) (al-maṣdar al-ʿāmil) without what it governs."},
    {"type": "matn",
     "ar": "فلا يجوز في نحو: «عجبت من دق القصار الثوب» أن يخبر بـ«الذي» عن «دق القصار» بدون الثوب،",
     "en": "So in such as “ʿajibtu min daqqi al-qaṣṣāri al-thawba” (I marvelled at the fuller’s beating the garment) one may not report by means of “alladhī” about “daqq al-qaṣṣār” without “al-thawb”,"},
    {"type": "matn",
     "ar": "لأنه يؤدي إلى أن يعمل الضمير الذي جعل في موضع «دق القصار» عاملا في الثوب، بخلاف «الذي عجبت منه دق القصار الثوب».",
     "en": "because that would lead to the pronoun placed in the position of “daqq al-qaṣṣār” governing “al-thawb”; unlike “alladhī ʿajibtu minhu daqqu al-qaṣṣāri al-thawba” (that at which I marvelled is the fuller’s beating the garment)."},
    {"type": "matn",
     "ar": "(و) كذلك امتنع في (الحال[[٤]])؛ لأن الحال يجب أن تكون نكرة، فلا يجوز أن يقع الضمير الذي هو معرفة في موضعه بالحالية.",
     "en": "(And) likewise it is impossible in the case of (the circumstantial qualifier) (ḥāl), because the ḥāl must be indefinite, so the pronoun, which is definite, may not occur in its position as a ḥāl."},
    {"type": "matn",
     # REVIEW: «فيبقي» printed with a dotted yāʾ; one expects «فيبقى»; transcribed as printed.
     "ar": "(و) كذلك امتنع في (الضمير المستحق لغيرها[[٥]]) أي: لغير كلمة «الذي» لامتناع تصدير «الذي» لاستلزام ذلك عود الضمير إليها، فيبقي ذلك الغير بلا ضمير.",
     "en": "(And) likewise it is impossible in the case of (the pronoun due to something other than it), that is, other than the word “alladhī”, because it is impossible to begin with “alladhī”, since that entails the pronoun’s referring back to it, so that other thing would be left without a pronoun."},
    {"type": "matn",
     "ar": "(و) كذلك امتنع في (الاسم المشتمل عليه) أي: على الضمير المستحق لغيرها،",
     "en": "(And) likewise it is impossible in the case of (the noun that contains it), that is, contains the pronoun due to something other than it,"},
    {"type": "matn",
     "ar": "نحو قولك: «زيد ضربت غلامه»، فلا يصح الإخبار عن «غلامه» بأن يقال: «الذي زيد ضربته غلامه»؛",
     "en": "as in your saying “Zaydun ḍarabtu ghulāmahu” (Zayd, I struck his servant); so it is not valid to report about “ghulāmahu” by saying “alladhī Zaydun ḍarabtuhu ghulāmuhu”,"},
    {"type": "matn",
     "ar": "لأنك إذا جعلت الضمير عائدا إلى الموصول بقي المبتدأ بلا عائد، وإذا جعلته عائدا إلى المبتدأ بقي الموصول بلا عائد، وكل منهما ممتنع.",
     "en": "because if you make the pronoun refer back to the relative noun, the subject (mubtadaʾ) is left without a referring pronoun, and if you make it refer back to the subject, the relative noun is left without a referring pronoun; and each of the two is impossible."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لو قال: «في ضمير المبهم» ليشمل مثل ضمير «نعم رجلا وربه رجلا» لكان أعم فائدة.",
     "en": "Had he said “in the case of the vague pronoun”, so as to include such as the pronoun of “niʿma rajulan” and “rubbahu rajulan”, it would have been of more general benefit."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وكذا ألفاظ التأكيد في الأشهر؛ إذ تلك الألفاظ معتبرة في التأكيد، فلا يفيد الضمير ما أفادته.",
     "en": "So too the words of corroboration (taʾkīd), on the better-known view, since those words are specifically required for corroboration, so the pronoun does not convey what they convey."},
    {"type": "pair",
     "ar": "ويجب أن يكون الضمير مفيدا لما يفيده المخبر عنه.",
     "en": "Yet the pronoun must convey what the thing reported about conveys."},
    {"type": "pair",
     "ar": "وكذا عطف البيان دون المعطوف. وأما البدل والمبدل منه فقد اختلف فيهما.",
     "en": "So too the explicative apposition (ʿaṭf al-bayān) without the [noun] it follows. As for the substitute (badal) and that for which it substitutes, there is disagreement about them."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وكذا الصفة العاملة. وأما الإخبار عن قائم في زيد قائم، فإنما يجوز إذا لم تعمله في الضمير المستكن نظرا إلى كونه في الأصل اسما مستغنيا عن الفاعل.",
     "en": "So too the governing qualifier. As for reporting about “qāʾim” in “Zaydun qāʾimun”, it is permitted only if you do not make it govern the latent pronoun, in view of its being in origin a noun that has no need of an agent."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأولى ما يجب تنكيره، فاعرفه، يزد لك تمييزا.",
     "en": "It would be better [to say] “whatever must be indefinite”; so know it, and it will increase your discernment."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: الذي استحق غيرها.",
     "en": "That is: [the pronoun] which something other than it has a claim to."},
]
