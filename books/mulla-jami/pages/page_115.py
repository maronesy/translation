# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 115 (printed ١١٤)."""

PAGE_NUMBER = 115
PRINTED_PAGE = "١١٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The main commentary (matn) ----------------
    {"type": "matn",
     "ar": "المبنيات، فكيف يتصور فيها منع الصرف الذي هو من أحكام المعربات؟",
     "en": "the indeclinables (mabniyyāt); so how can the prevention of full inflection (manʿ al-ṣarf) — which is among the properties of declinable nouns (muʿrabāt) — be conceived to occur in them?"},
    {"type": "matn",
     "ar": "فإن قلت: كان على المصنف[[١]] أن يقول: وألا يكون الجزء الثاني من المركب صوتا، ولا متضمنا بحرف العطف ليخرج مثل: «سيبويه ونفطويه»، ومثل: «خمسة عشر، ستة عشر» علمين[[٢]]؟",
     "en": "If you say: the author ought to have said, “and that the second part of the compound be neither a mere sound nor include a conjunctive particle,” so as to exclude the likes of “Sībawayh” and “Nifṭawayh,” and the likes of “fifteen” and “sixteen” [used] as proper names?"},
    {"type": "matn",
     "ar": "قلنا: كأنه اكتفى[[٣]] في ذلك[[٤]] بما ذكره فيما بعد[[٥]]، إنهما من قبيل المبنيات. وأما الأعلام المشتملة على الإسناد، فلم يذكر بناءها أصلا، فلذلك احتاج إلى إخراجها.",
     "en": "We reply: it is as though he deemed sufficient, in that regard, what he mentions later — namely that both belong to the category of the indeclinables. As for proper names that comprise a predicative relation (isnād), he did not mention their indeclinability at all, and for that reason he needed to exclude them."},
    {"type": "matn",
     "ar": "(مثل: بعلبك) فإنه علم لبلدة[[٦]] مركب من «بعل»، وهو اسم صنم و«بك» وهو اسم صاحب هذه البلدة، جعلا اسما واحدا من غير أن يقصد[[٧]] بينهما نسبة[[٨]] إضافية أو إسنادية أو غيرهما[[٩]].",
     "en": "(Such as: Baʿlabakk) — for it is a proper name of a town, compounded of “Baʿl,” which is the name of an idol, and “Bakk,” which is the name of the founder of this town; the two were made into a single name without any relation — genitive, predicative, or other than these — being intended between them."},

    # ---------------- Section heading ----------------
    {"type": "section", "ar": "[الألف والنون]",
     "en": "The Alif and the Nūn"},

    {"type": "matn",
     "ar": "(الألف والنون[[١٠]]) المعدودان من أسباب منع الصرف، تسميان مزيدتين؛ لأنهما من الحروف الزوائد[[١١]]، وتسميان مضارعتين أيضا، لمضارعتهما لألفي التأنيث[[١٢]]",
     "en": "(The alif and the nūn) — reckoned among the causes preventing full inflection — are called “augmentative” (mazīdatān), because they belong to the augmentative letters; and they are also called “resembling” (muḍāriʿatān), on account of their resemblance to the two alifs of the feminine —"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كلمة «على» تستعمل للوجوب.",
     "en": "The word ʿalā (“ought”) is used to denote obligation."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيد خمسة عشر وستة عشر بكونهما علمين، مع أن العلمية لا بد فيها كلها ليكون من موارد النقض،",
     "en": "He qualified “fifteen” and “sixteen” by their being proper names — although being a proper name is indispensable in all of them — so that it may serve as an instance of the counter-example;"},
    {"type": "pair",
     "ar": "إلا أنه اكتفى بسيبويه ونفطويه لكونهما مشهورين بالعلمية، أو ثلاثة باعتبار النوعين، أي: الذي كان الجزء الثاني منه صوتا، والذي كان متضمنا لحرف العطف.",
     "en": "except that he deemed sufficient [the mention of] “Sībawayh” and “Nifṭawayh,” because these two are well known as proper names — or [he mentioned] three, taking into account the two kinds: that whose second part is a mere sound, and that which includes a conjunctive particle."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما قال: «كأنه»؛ لأن المذكور فيما بعد مع بعده حكم لما يتضمنه حرف العطف بالفعل لا لما يتضمنه بحسب الأصل.",
     "en": "He said “it is as though” only because what is mentioned later — besides its being remote — is a ruling concerning that which actually includes the conjunctive particle, not concerning that which includes it merely by original derivation."},
    {"type": "pair",
     "ar": "ومن الجائز التخالف في الحكم. ولذا ذهب بعضهم إلى أن نحو: خمسة عشر علما معرب غير منصرف.",
     "en": "And divergence in the ruling is admissible. For this reason some have held that the likes of “fifteen” [used] as a proper name is declinable but non-inflecting (ghayr munṣarif)."},
    {"type": "pair",
     "ar": "ومن ههنا ينقدح جواب آخر هو أن المصنف وافقهم في منع الصرف.",
     "en": "And from here another answer suggests itself: namely, that the author agreed with them in [ruling] the prevention of full inflection."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: في إخراج مثل سيبويه وخمسة عشر.",
     "en": "That is: in the exclusion of the likes of “Sībawayh” and “fifteen.”"},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: في بحث المبنيات.",
     "en": "That is: in the discussion of the indeclinables."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه أنه إذا كان بعلبك علما لبلدة يجوز أن يكون منع صرفه للعلمية والتأنيث كماه وجور، فلم يكن مثالا قطعيا للتركيب المؤثر في منع الصرف.",
     "en": "Against this it may be objected that, since “Baʿlabakk” is a proper name of a town, the prevention of its inflection could well be on account of being a proper name and [grammatical] femininity — as with Māh and Jūr — so it is not a decisive example of composition (tarkīb) exerting an effect in preventing inflection."},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "بل من غير نقل عن مركب مستعمل في معنى، فيكون علما على الارتجال.",
     "en": "Rather, [it was made a single name] without being transferred from a compound used in some meaning, so that it is a proper name coined ex nihilo (irtijāl)."},

    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لا في الحال ولا في الأصل، بخلاف «عبد الله» علما، فإنه قصد بين جزئيه نسبة في الأصل.",
     "en": "Neither in its present state nor in its origin — unlike “ʿAbd Allāh” as a proper name, for a relation between its two parts was intended in its origin."},

    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "لا حاجة إلى هذا، فإن وجود نسبة غير إضافية وإسنادية لا يضر في تأثير التركيب، فلا حاجة إلى نفيها.",
     "en": "There is no need for this [qualification], for the existence of a relation other than a genitive or predicative one does no harm to the effect of the composition, so there is no need to negate it."},

    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "قيل: الواو بمعنى «مع». ولك اعتبار العطف أولا، ثم الحكم عليه بقوله: إن كانا إلى آخره.",
     "en": "It is said: the wāw here means “together with” (maʿa). You may, however, take it as a conjunction first, and then [apply] the ruling upon it by his words, “if the two are…,” to the end."},

    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "بالفعل. فلو احتمل لفظ نونه الأصالة جاز صرفه كحسان لجواز أن يكون من الحسن، كما جاز أن يكون من الحس ويمنع حينئذ.",
     "en": "[Augmentative] actually. For if the nūn of a word could possibly be original, its full inflection would be permissible — as with “Ḥassān,” which may be derived from ḥusn (beauty), whereby it is inflected, just as it may be from ḥiss (sensation), whereby it is then prevented [from inflection]."},

    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "أي: المقصورة والممدودة.",
     "en": "That is: the shortened alif (al-maqṣūra) and the extended alif (al-mamdūda)."},
]
