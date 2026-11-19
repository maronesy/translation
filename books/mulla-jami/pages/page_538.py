# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 538 (printed ٥٣٧)."""

PAGE_NUMBER = 538
PRINTED_PAGE = "٥٣٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وفاعله) أي:» at the foot of PDF p. 537 (mid-sentence).
    {"type": "matn",
     "ar": "فاعل هذا الفعل («ذا»، ولا يتغير[[١]]) أي: «حبذا»، أو فاعله، أو «ذا» عما هو عليه،",
     "en": "…the agent of this verb, (is “dhā”; and it does not change), that is, “ḥabbadhā”, or its agent, or “dhā”, from what it is;"},
    {"type": "matn",
     "ar": "فلا يثنى ولا يجمع ولا يؤنث إذا كان المخصوص مثنى أو جمعا أو مؤنثا؛ لجريها مجرى الأمثال[[٢]] التي لا تتغير،",
     "en": "so it is not made dual, plural or feminine when the specified term is dual, plural or feminine, because it runs the course of proverbs, which do not change;"},
    {"type": "matn",
     "ar": "فيقال: «حبذا الزيدان، وحبذا الزيدون، وحبذا هند».",
     "en": "so one says “ḥabbadhā al-Zaydāni”, “ḥabbadhā al-Zaydūna”, “ḥabbadhā Hindun”."},
    {"type": "matn",
     "ar": "(وبعده) أي: بعد «حبذا» (المخصوص. وإعرابه) أي: إعراب مخصوص «حبذا» (كإعراب مخصوص «نعم») على الوجهين المذكورين.",
     "en": "(And after it), that is, after “ḥabbadhā”, (comes the specified term; and its inflection), that is, the inflection of the specified term of “ḥabbadhā”, (is like the inflection of the specified term of “niʿma”), on the two analyses mentioned."},
    {"type": "matn",
     "ar": "(ويجوز أن يقع قبل المخصوص) أي: مخصوص «حبذا» (أو بعده) أي: بعد مخصوصه (تمييز، أو حال[[٣]] على وفق مخصوصه) في الإفراد والتثنية والجمع والتذكير والتأنيث،",
     "en": "(And there may occur before the specified term), that is, the specified term of “ḥabbadhā”, (or after it), that is, after its specified term, (a specification (tamyīz) or a circumstantial (ḥāl) in accordance with its specified term), in singular, dual and plural, masculine and feminine,"},
    {"type": "matn",
     "ar": "نحو: «حبذا رجلا زيد، وحبذا زيد رجلا، وحبذا راكبا زيد، وحبذا زيد راكبا، وحبذا رجلين أو راكبين الزيدان، وحبذا الزيدان رجلين أو راكبين، وحبذا امرأة هند، وحبذا هند امرأة».",
     "en": "as in “ḥabbadhā rajulan Zaydun”, “ḥabbadhā Zaydun rajulan”, “ḥabbadhā rākiban Zaydun”, “ḥabbadhā Zaydun rākiban”, “ḥabbadhā rajulayni” or “rākibayni al-Zaydāni”, “ḥabbadhā al-Zaydāni rajulayni” or “rākibayni”, “ḥabbadhā imraʾatan Hindun”, and “ḥabbadhā Hindun imraʾatan”."},
    {"type": "matn",
     "ar": "والعامل في التمييز أو الحال ما في «حبذا» من الفعلية[[٤]]، وذو الحال هو «ذا» لا «زيد»؛",
     "en": "What governs the specification or the circumstantial is the verbal element in “ḥabbadhā”, and the possessor of the circumstantial (dhū al-ḥāl) is “dhā”, not “Zayd”,"},
    {"type": "matn",
     "ar": "لأن زيدا مخصوص، والمخصوص لا يجيء إلا بعد تمام المدح والركوب من تمامه، فالراكب حال من الفاعل لا من المخصوص[[٥]].",
     "en": "because Zayd is the specified term, and the specified term comes only after the praise is complete, and the riding belongs to its completion; so “rākib” is a circumstantial of the agent, not of the specified term."},

    {"type": "section", "ar": "[الحرف]",
     "en": "The Particle (al-Ḥarf)"},

    {"type": "matn",
     "ar": "(الحرف: ما دل على معنى في غيره) أي: كلمة دلت على معنى حاصل في غيرها",
     "en": "(The particle (ḥarf) is that which signifies a meaning in something other than itself), that is, a word that signifies a meaning realized in something other than it…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ومن هذا الباب زعم بعض أنه بعد التركيب صار اسما بمعنى «حبيب» خبر لما بعده، فمعنى حبذا الأمير هو حبيب، واختاره أبو علي وصاحب القاموس،",
     "en": "On this matter some claimed that after compounding it became a noun meaning “ḥabīb” (beloved), predicate of what follows it, so that the meaning of “ḥabbadhā al-amīru” is “he is beloved”; Abū ʿAlī and the author of al-Qāmūs chose this;"},
    {"type": "pair",
     "ar": "أو مبتدأ خبره ما بعده، وإليه ذهب المبرد.",
     "en": "or [it became] a subject whose predicate is what follows it; al-Mubarrad held this."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "كأنهم عاملوها معاملة المضمر في أنه لا يختلف باختلاف الممدوح مثنى ومجموعا ومؤنثا",
     "en": "It is as though they treated it like the concealed pronoun, in that it does not vary with the variation of the one praised, as dual, plural or feminine;"},
    {"type": "pair",
     "ar": "وشبهه بالمضمر في نحو: نعم رجلا أقوى منه بالظاهر في «نعم الرجل زيد»، لزيادة إبهامه وعدم كونه اسما ظاهرا.",
     "en": "and its resemblance to the pronoun in “niʿma rajulan” is stronger than its resemblance to the explicit noun in “niʿma al-rajulu Zaydun”, because of its greater vagueness and its not being an explicit noun."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فإن قصد تقييد المبالغة في مدح المخصوص بوصف كان المنصوب حالا نحو: «حبذا هند» مواصلة أي: في حال مواصلتها،",
     "en": "If restricting the intensity of the praise of the specified term to a quality is intended, the accusative is a circumstantial, as in “ḥabbadhā Hindun” muwāṣilatan, that is, in the state of her keeping company;"},
    {"type": "pair",
     "ar": "وإن قصد بيان جنس المبالغة في مدحه كان تمييزا نحو: «حبذا زيدا راكبا، وحبذا زيد رجلا»",
     "en": "and if explaining the genus of the intensity in his praise is intended, it is a specification, as in “ḥabbadhā Zaydan rākiban” and “ḥabbadhā Zaydun rajulan”."},
    {"type": "pair",
     "ar": "ولا يلزم الفصل بالأجنبي؛ لأن المخصوص ليس بأجنبي لاتحاده بالفاعل.",
     "en": "Separation by an extraneous element does not follow, because the specified term is not extraneous, being one with the agent."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأولى من الفعل؛ لأن العامل هو حب؛ لأنه فعل، وعلى هذا القياس العامل في التمييز في «نعم رجلا»،",
     "en": "Better would be “of the verb”, because what governs is “ḥabba”, since it is a verb; and by the same analogy is the governor of the specification in “niʿma rajulan”."},
    {"type": "pair",
     "ar": "نعم والظاهر أن العامل في التمييز عن الذات المذكورة المبهمة كما في «رطل زيتا»، فالعامل كلمة «ذا»، أو الضمير المبهم كما في «ربه رجلا».",
     "en": "Granted; yet apparently what governs is [that of] the specification of a mentioned vague entity, as in “raṭlun zaytan” (a pound of oil); so the governor is the word “dhā”, or the vague pronoun, as in “rubbahu rajulan”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فيه مصادرة؛ لأن المدعى أن «ذا» ذو الحال لا زيد، وهو بعينه أن الراكب حال عن الفاعل لا عن المخصوص،",
     "en": "In it is a begging of the question (muṣādara), because what is claimed is that “dhā” is the possessor of the circumstantial, not Zayd, and this is exactly that “rākib” is a circumstantial of the agent, not of the specified term;"},
    {"type": "pair",
     "ar": "فالصحيح فالراكب حال عن الفاعل لا عن المخصوص، كما في بعض النسخ.",
     "en": "so the correct reading is “so rākib is a circumstantial of the agent, not of the specified term”, as in some copies."},
]
