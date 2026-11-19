# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 182 (printed ١٨١)."""

PAGE_NUMBER = 182
PRINTED_PAGE = "١٨١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "يجوز فيما بعدها الرفع ما لم يتكرر، ولا تكرار في البيت.",
     "en": "…permit the nominative in what follows it so long as it is not repeated; and there is no repetition in the verse."},
    {"type": "matn",
     "ar": "اعلم أن المراد بالمسند[[١]] والمسند إليه في هذه التعريفات، ما يكون مسندا أو مسندا إليه بالأصالة لا بالتبعية بقرينة ذكر التوابع فيما بعد، فلا ينتقض بالتوابع.",
     "en": "Know that what is meant by “the predicate” (al-musnad) and “that to which [something] is predicated” (al-musnad ilayhi) in these definitions is what is a predicate or a subject of predication primarily, not by way of dependence (tabaʿiyya), as indicated by the mention of the dependents (tawābiʿ) later on; so [the definitions] are not contradicted by the dependents."},

    {"type": "section", "ar": "[ المنصوبات ]",
     "en": "The Accusatives (al-Manṣūbāt)"},

    {"type": "matn",
     "ar": "ولما فرغ من المرفوعات شرع[[٢]] في المنصوبات، وقدمها على المجرورات، لكثرتها ولخفة النصب[[٣]]،",
     "en": "Having finished with the nominatives, he began on the accusatives, and he placed them before the genitives because of their number and because of the lightness of the accusative,"},
    {"type": "matn",
     "ar": "فقال: (المنصوبات: هو ما اشتمل على علم المفعولية). قد تبين شرحه بما ذكر في المرفوعات.",
     "en": "and he said: (The accusatives: it is that which contains the mark of being an object [ʿalam al-mafʿūliyya]). Its explanation has become clear from what was said regarding the nominatives."},
    {"type": "matn",
     "ar": "والمراد بعلم المفعولية: علامة كون الاسم مفعولا[[٤]] حقيقة أو حكما،",
     "en": "What is meant by “the mark of being an object” is the sign of the noun’s being an object, really (ḥaqīqatan) or by assimilated status (ḥukman)."},
    {"type": "matn",
     "ar": "وهي أربع: الفتحة والكسرة، والألف، والياء، نحو: «رأيت زيدا، ومسلمات، وأباك، ومسلمين، ومسلمين».",
     "en": "They are four: the fatḥa, the kasra, the alif and the yāʾ; as in: “I saw Zayd, Muslim women, your father, two Muslims, and Muslims” (raʾaytu Zaydan, wa-muslimātin, wa-abāka, wa-muslimayni, wa-muslimīna)."},

    {"type": "section", "ar": "[ المفعول المطلق ]",
     "en": "The Absolute Object (al-Mafʿūl al-Muṭlaq)"},

    {"type": "matn",
     "ar": "(فمنه) أي: من المنصوب[[٥]] أو مما اشتمل على علم المفعولية[[٦]] (المفعول المطلق)",
     "en": "(Among them)—that is, among the accusative, or among what contains the mark of being an object—(is the absolute object [al-mafʿūl al-muṭlaq])."},
    {"type": "matn",
     "ar": "سمي به، لصحة إطلاق صيغة المفعول عليه[[٧]] من غير تقييده بـ«الباء، أو",
     "en": "It was so named because the form “object” (mafʿūl) may validly be applied to it without restricting it by “the bāʾ,” or…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا التعرض مبني على الغفلة عما ذكره في تعريف الفاعل.",
     "en": "Raising this [point] rests on inattention to what he mentioned in the definition of the agent (fāʿil)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: أراد أن يشرع.",
     "en": "That is: he wished to begin."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وذلك باعتبار الخفة التي هي الأصل في الإعراب، والخفيف يعلو على الثقيل،",
     "en": "That is in consideration of lightness, which is the default in inflection (iʿrāb); and the light takes precedence over the heavy."},
    {"type": "pair",
     "ar": "ولأن مناسبة المنصوب بالمرفوع أكثر من مناسبته بالمجرور من حيث اشتمال تعريفيهما على الفاعلية والمفعولية اللتين هما كالمتضايفين، فتأمل،",
     "en": "And because the affinity of the accusative with the nominative is greater than its affinity with the genitive, inasmuch as their two definitions contain agency and objecthood, which are like two correlatives (mutaḍāyifayn)—so reflect—"},
    {"type": "pair",
     "ar": "ومن حيث تلازمهما في أكثر الأحوال، وهي الأفعال المتعدية.",
     "en": "and inasmuch as the two are concomitant in most cases, namely [with] transitive verbs."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: من حيث إنه علامة كون الاسم مفعولا،",
     "en": "That is: inasmuch as it is a sign of the noun’s being an object;"},
    {"type": "pair",
     "ar": "فلا يبطل طرد تعريف علم المفعولية، ولا طرد تعريف المنصوبات بـ«مررت بمسلمات ومسلمين ومسلمين» بل «مررت بزيد».",
     "en": "so the exclusiveness (ṭard) of the definition of the mark of objecthood is not invalidated, nor the exclusiveness of the definition of the accusatives, by “I passed by Muslim women, two Muslims, and Muslims,” or even by “I passed by Zayd.”"},
    {"type": "pair",
     "ar": "وقوله: وهي أي: علامة كون الاسم مفعولا لا مع قيد الحيثية، فلا حاجة إلى تقييد الأمور الأربعة بالحيثية.",
     "en": "His words “and they are” [refer to] the sign of the noun’s being an object without the qualification “inasmuch as” (qayd al-ḥaythiyya); so there is no need to restrict the four things by “inasmuch as.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: أن الضمير راجع إلى المنصوب المذكور في ضمن المنصوبات موافقا لضمير هو في قوله: ما اشتمل،",
     "en": "He means that the pronoun refers back to “the accusative” mentioned implicitly within “the accusatives,” in agreement with the pronoun “huwa” in his words “that which contains”;"},
    {"type": "pair",
     "ar": "وهو المناسب باعتبار جعل القسم موافقا لما جعل معرفا.",
     "en": "and this is what is fitting, in consideration of making the division agree with what was made the thing defined."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ليوافق ضمير «اشتمل» الراجع إلى «ما»، وهو المناسب باعتبار قرب المرجع.",
     "en": "So as to agree with the pronoun of “ishtamala,” which refers back to “mā”; and this is what is fitting, in consideration of the nearness of the antecedent."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لغة. وأما اصطلاحا فيصح الإطلاق على كل من الخمسة،",
     "en": "Lexically. As for technical usage, the term may validly be applied to each of the five;"},
    {"type": "pair",
     "ar": "وهو ما قرن بفعل لفائدة، ولم يسند إليه ذلك الفعل، وتعلق به تعلقا مخصوصا.",
     "en": "[technically,] it is that which is joined to a verb for some benefit, without that verb being predicated of it, and to which [the verb] is connected in a particular way."},
    {"type": "pair",
     "ar": "ولا يخفى أنه ينتقض بمفعول ما لم يسم فاعله، فإنه مفعول ولم يشمله التعريف،",
     "en": "It is not hidden that this is contradicted by the object of the verb whose agent is not named (mafʿūl mā lam yusamma fāʿiluhu), for it is an object, yet the definition does not include it;"},
    {"type": "pair",
     "ar": "إلا أن يقال: إطلاق المفعول عليه باعتبار أنه كان في الأصل مفعولا اصطلاحيا.",
     "en": "unless it be said that “object” is applied to it in view of its having originally been an object in the technical sense."},
]
