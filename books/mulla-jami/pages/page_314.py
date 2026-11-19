# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 314 (printed ٣١٣)."""

PAGE_NUMBER = 314
PRINTED_PAGE = "٣١٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «"عوذا" -بالذال المعجمة- جمع عائذ أي:» at the foot of PDF p. 313.
    {"type": "matn",
     "ar": "حديثات النتائج حال من المائة، «يزجى» -بالزاي المعجمة والجيم- على صيغة المعلوم المذكر أي: «يسوق»، وفاعله ضمير راجع إلى العبد، و«أطفالها» منصوب على المفعولية،",
     "en": "…[that is,] recently delivered of their young, a circumstantial qualifier (ḥāl) of “the hundred”; “yuzjī”—with the dotted zāy and the jīm—is in the masculine active form, that is, “he drives,” its agent (fāʿil) being a pronoun referring back to “the slave,” and “aṭfālahā” (their young) is accusative as its object;"},
    {"type": "matn",
     "ar": "أو على صيغة المجهول المؤنث، و«أطفالها» مرفوع على أنه مفعول ما لم يسم فاعله،",
     "en": "or it is in the feminine passive form, and “aṭfāluhā” is nominative as the object whose agent is not named (mafʿūl mā lam yusamma fāʿiluhu)."},
    {"type": "matn",
     "ar": "وحقيقة الأمر لا ينكشف إلا بعد معرفة حركة حرف الروي من القصيدة.",
     "en": "The truth of the matter is disclosed only once the vowel of the rhyme letter (ḥarf al-rawī) of the ode is known."},
    {"type": "matn",
     "ar": "وإما لأنه قاسه[[١]] على «الضارب الرجل والضاربك».",
     "en": "Or [al-Farrāʾ held this] because he drew an analogy between it and “al-ḍāribu l-rajuli” and “al-ḍāribuka.”"},
    {"type": "matn",
     "ar": "فأجاب المصنف عنه بقوله: (وإنما جاز «الضارب الرجل») يعني: كان القياس عدم جوازه لانتفاء التخفيف لزوال التنوين باللام[[٢]]،",
     "en": "The author answered this with his words: (“al-ḍāribu l-rajuli” is permitted only), meaning: analogy required that it not be permitted, since lightening (takhfīf) is absent, the tanwīn having already been removed by the article (lām);"},
    {"type": "matn",
     "ar": "لكنه جاز (حملا على) الوجه (المختار في «الحسن الوجه») وهو جر «الوجه» بالإضافة، وفيه وجهان آخران[[٣]]: رفعه على الفاعلية، ونصبه على التشبيه بالمفعولية،",
     "en": "but it was permitted (by assimilation to) the (preferred) construction (in “al-ḥasanu l-wajhi”), which is the genitive of “al-wajh” by annexation (iḍāfa); there are two other constructions for it: its nominative as agent, and its accusative by resemblance to an object."},
    {"type": "matn",
     "ar": "ووجه الحمل اشتراكهما في كون المضاف صفة والمضاف إليه جنسا معرفين باللام،",
     "en": "The ground of the assimilation is their sharing in the annexed term being an adjective and the term annexed to being a generic noun, both made definite by the article;"},
    # REVIEW: the sense requires «وهذا الاشتراك [منتف] بين…» or similar; the print has no negation; transcribed as printed.
    {"type": "matn",
     "ar": "وهذا الاشتراك بين «الضارب زيد والحسن الوجه»، فقياسه عليه قياس مع الفارق",
     "en": "and this sharing [is lacking] between “al-ḍāribu Zaydin” and “al-ḥasanu l-wajhi,” so the analogy of the one to the other is an analogy despite a distinguishing difference (qiyās maʿa l-fāriq)."},
    {"type": "matn",
     "ar": "(و«الضاربك») يعني: إنما جاز «الضاربك» مع أن القياس عدم جوازه لما عرفت.",
     "en": "(And “al-ḍāribuka”), meaning: “al-ḍāribuka” is permitted only [by assimilation], although analogy requires that it not be permitted, for the reason you have learned."},
    {"type": "matn",
     "ar": "(و) كذا (شبهه) وهو «الضاربي والضاربه» وغيرهما (فيمن قال) أي: في قول من قال يعني: سيبويه وأتباعه[[٤]]",
     "en": "(And) likewise (what resembles it), namely “al-ḍāribī” and “al-ḍāribuhu” and the like, (according to whoever said), that is, in the view of whoever said—meaning Sībawayh and his followers—"},
    {"type": "matn",
     "ar": "(إنه) أي: «الضارب» في «الضاربك» (مضاف) دون من قال: «إنه غير مضاف» -والكاف منصوب المحل على المفعولية، والتنوين محذوف لاتصال الضمير لا للإضافة،",
     "en": "(that it), that is, “al-ḍārib” in “al-ḍāribuka,” (is annexed), not according to whoever said “it is not annexed”—the kāf being accusative in place as object, and the tanwīn dropped because of the attached pronoun, not because of annexation—"},
    {"type": "matn",
     "ar": "فإنه لا يحتاج في جوازه إلى الحمل[[٥]]- (حملا) أي:",
     "en": "for on that view its permissibility does not require assimilation. (By assimilation), that is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "عطف على قوله: إما لأنه توهم عند شرح قوله: خلافا للفراء.",
     "en": "Coordinated with his words “either because he imagined,” in the commentary on his words “contrary to al-Farrāʾ.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يكفي في إثبات انتفاء التخفيف، بل لا بد من ضميمة انتفاء ما يحذف من المضاف إليه للإضافة كما في الحسن الوجه.",
     "en": "This does not suffice to establish the absence of lightening; one must add the absence of what is dropped from the term annexed to on account of annexation, as in “al-ḥasanu l-wajhi.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أما الرفع، فقبيح لخلو الصفة عن الضمير العائد.",
     "en": "As for the nominative, it is unsound, because the adjective is then left without a resumptive pronoun."},
    {"type": "pair",
     "ar": "وأما النصب، ففيه تمحل حيث جعل الفاعل مشبها بالمفعول فنصب.",
     "en": "As for the accusative, it is forced (tamaḥḥul), since the agent is made to resemble the object and so put in the accusative."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "تبع فيه جماعة من الشارحين حيث فسروا كلام المصنف هكذا بناء على ما نقل عن سيبويه من جواز الجر في الضاربك،",
     "en": "In this he followed a group of the commentators, who interpreted the author’s words in this way on the basis of what is reported from Sībawayh, namely that the genitive is permitted in “al-ḍāribuka”;"},
    {"type": "pair",
     "ar": "لكن المشهور من مذهبه أنه لا يجوز فيه إلا النصب قياسا على المظهر.",
     "en": "but the well-known position of his school is that only the accusative is permitted in it, by analogy with the overt noun."},
    {"type": "pair",
     "ar": "ولذا لم يسند الشيخ الرضي إلى سيبويه إلا ما هو المشهور من مذهبه، وأسند القول بالجواز إلى الرماني والمبرد في أحد قوليه وجار الله.",
     "en": "For this reason Shaykh al-Raḍī attributed to Sībawayh only what is well known of his position, and attributed the view that it is permitted to al-Rummānī, to al-Mubarrad in one of his two opinions, and to Jār Allāh [al-Zamakhsharī]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أشار إلى إفادة قوله: فيمن قال.",
     "en": "He points to what his words “according to whoever said” convey."},
    {"type": "pair",
     "ar": "والأظهر أنه إشارة إلى رد قياس المبرد على الضاربك من وجه آخر، وهو منع كونه مضافا.",
     "en": "The more evident reading is that it points to the rejection of al-Mubarrad’s analogy with “al-ḍāribuka” on another ground, namely denying that it is annexed."},
]
