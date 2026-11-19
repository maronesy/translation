# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 60 (printed ٥٩)."""

PAGE_NUMBER = 60
PRINTED_PAGE = "٥٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "على الضمائر، وأسماء الإشارة، وغيرها[[١]]، كالموصولات، وكذلك سائر الخواص الخمس[[٢]] المذكورة ههنا.",
     "en": "[The definite particle does not enter] upon the pronouns, the demonstrative nouns, and others such as the relative nouns (mawṣūlāt); and likewise [the same holds for] the rest of the five properties mentioned here."},
    {"type": "matn",
     "ar": "٢- (و) منها: دخول (الجر)[[٣]]. وإنما اختص دخول الجر بالاسم؛ لأنه[[٤]] أثر حرف الجر[[٥]] في المجرور به[[٦]] لفظا، وفي المجرور به تقديرا، كما في الإضافة المعنوية.",
     "en": "2 — And among them [the properties] is the entry of (the genitive, al-jarr). The entry of the genitive is restricted to the noun only because it [the jarr] is the effect (athar) of the genitive particle in the term governed by it explicitly, and in the term governed by it implicitly, as in conceptual annexation (al-iḍāfa al-maʿnawiyya)."},
    {"type": "matn",
     "ar": "ودخول حرف الجر لفظا أو تقديرا يختص بالاسم؛ لأنه[[٧]] لإفضاء معنى الفعل إلى الاسم، فينبغي أن يدخل الاسم، ليفضي معنى الفعل إليه.",
     "en": "And the entry of the genitive particle — whether explicitly or implicitly — is [itself] restricted to the noun, because it [is coined] for conveying the meaning of the verb to the noun; so it ought to enter upon the noun, in order to convey the meaning of the verb to it."},
    {"type": "matn",
     "ar": "وأما الإضافة اللفظية[[٨]]، فهي فرع للمعنوية، فينبغي ألا يخالف الأصل، بأن يختص[[٩]] بما يخالف ما يختص به الأصل، أعني: الفعل، أو يزيد عليه[[١٠]] بأن يعم الاسم والفعل.",
     "en": "As for verbal annexation (al-iḍāfa al-lafẓiyya), it is a branch of the conceptual [annexation], so it ought not to diverge from the root — [it would diverge] by being peculiar to that which differs from what the root is peculiar to, namely the verb, or by exceeding it [the root] through comprising both the noun and the verb."},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: غير الضمائر.",
     "en": "That is, [others] than the pronouns."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "اعلم أن تلك الخواص كما أنها ليست شاملة ليست أكثرها خاصة حقيقية، بل إضافية؛ لوجودها في غير الاسم إذا لم يرد به معناه، نعم إذا أريد به المعنى لا يوجد فيه. ولذلك طوى بيان الاطراد والانعكاس.",
     "en": "Know that those properties — just as they are not all-encompassing (shāmila) — most of them are not a real (ḥaqīqī) property but rather a relative (iḍāfī) one, on account of their occurrence in other than the noun when its meaning is not intended by it; yes — when the meaning is intended by it, [the property] is not found in it. For this reason he folded up [i.e., omitted] the exposition of co-extensiveness (iṭṭirād) and co-exclusiveness (inʿikās)."},
    {"type": "pair",
     "ar": "ثم اعلم أنه اختار هذه الخمس؛ لأن كلا منها متضمن لخواص كثيرة، فإن اللام متضمنة لأنواع التعريف، والجر متضمن لاختصاص حروف الجر، وهي كثيرة، والتنوين لاختصاص أصنافه ومعانيها، والإضافة لاختصاص كونه مضافا أو مضافا إليه، والتعريف والتخصيص والتخفيف، والإسناد إليه لاختصاص كونه موصوفا وذا حال ومفعولا ومميزا.",
     "en": "Then know that he chose these five because each of them comprises many properties: for the lām comprises the kinds of definiteness; the genitive comprises the peculiar governance of the genitive particles, which are many; the nunation, the peculiarity of its categories and their meanings; annexation, the peculiarity of [the noun’s] being the annexed term or the annexed-to term; and definiteness, particularization, and lightening (takhfīf); and predication-to-it, the peculiarity of [the noun’s] being qualified (mawṣūf), possessed of a circumstantial state (dhū ḥāl), an object (mafʿūl), and a specifier (mumayyaz)."},
    {"type": "pair",
     "ar": "وأيضا لتلك الخواص خواص ومزايا كثيرة مبنية في علم المعاني لا توجد في غيرها من الخواص.",
     "en": "Moreover, those properties have many [further] properties and merits, established in the science of rhetoric (ʿilm al-maʿānī), not found in the other properties."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أراد بالجر كما هو الظاهر الدال على الإضافة إليه. وحينئذ يكون عطفا على اللام لفظه أو محله.",
     "en": "By “al-jarr” he intended — as is apparent — [the genitive] that indicates annexation to it [the noun]. In that case it is conjoined to “the lām,” [in respect of] its wording (lafẓ) or its position (maḥall)."},
    {"type": "pair",
     "ar": "ولو أريد بالجر مصدر جر مجهولا كان عطفا على دخول اللام، وقس عليه التنوين.",
     "en": "But were “al-jarr” taken as the verbal noun of “jurra” [construed] in the passive, it would be conjoined to “the entry of the lām”; and measure the tanwīn by the same [rule]."},
    {"type": "pair",
     "ar": "وإنما قدم الجر على التنوين مع أن بينه وبين لام التعريف مناسبة التقابل؛ لأنهما إذا اجتمعا في كلمة كان التنوين متأخرا عنه في الوجود.",
     "en": "He put the genitive before the nunation — despite there being between it [the nunation] and the definite lām (lām al-taʿrīf) the fitness of mutual opposition (munāsabat al-taqābul) — because when the two [the definite lām and the tanwīn] combine in a single word, the tanwīn is posterior to it in existence."},
    {"type": "pair",
     "ar": "وأما تقديم اللام عليهما، فإن الصدر موقعها. وأما تقديم الثلاثة على ما بقي، فلأنها لفظية، وهي أظهر من المعنوية في الدلالة على الاختصاص.",
     "en": "As for putting the lām before both, it is because the front [of the enumeration] is its [proper] place. And as for putting the three [lām, jarr, tanwīn] before what remains, it is because they are verbal (lafẓiyya), and the verbal is more manifest than the conceptual in indicating peculiarity (ikhtiṣāṣ)."},
    {"type": "pair",
     "ar": "وأما تقديم الإسناد إليه على الإضافة، فلأنه مدار الكلام، ولتضمنه خواص كثيرة.",
     "en": "And as for putting “predication-to-it” before “annexation,” it is because it is the pivot of speech, and because it comprises many properties."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الجر.",
     "en": "That is, [the pronoun refers to] the genitive."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: حرف أثره الجر، أو حرف يجر معنى الفعل إلى الاسم، ويعضد الأول حرف الجزم.",
     "en": "That is, a particle whose effect is the genitive, or a particle that draws (yajurru) the meaning of the verb to the noun; and the first [interpretation] is supported by [the existence of] the particle of jussion (ḥarf al-jazm)."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: بحرف الجر.",
     "en": "That is, by the genitive particle."},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: حرف الجر وضع.",
     "en": "That is, the genitive particle was coined [for that purpose]."},

    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: أما الجر الذي ليس أثر حرف الجر كما في الإضافة اللفظية، فلأنها فرع للمعنوية، أو لأنه لا يكون إلا فيما كان فاعلا أو مفعولا، والفعل والحرف لا يكونان كذلك.",
     "en": "That is, as for the genitive (al-jarr) that is not the effect of the genitive particle — as in verbal annexation — [its restriction to the noun is] because it is a branch of the conceptual [annexation]; or because it occurs only in that which is an agent (fāʿil) or an object (mafʿūl), while the verb and the particle are not so."},

    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "بيان للمخالفة بأنها متصورة على وجهين: أحدهما: أن يختص بقسم مقابل للاسم، وهو الذي يختص به الإضافة المعنوية، وذلك القسم المقابل ليس إلا الفعل؛ لأن الحرف لعدم استقلال معناه غير صالح لأن يضاف إليه شيء. وثانيهما: أن يزيد على الاسم بأن يدخله والفعل.",
     "en": "An explanation of the divergence, [namely] that it is conceivable in two ways: the first, that it be peculiar to a category opposite to the noun — which is that to which conceptual annexation is peculiar — and that opposite category is nothing but the verb, because the particle, owing to the non-independence of its meaning, is unfit for anything to be annexed to it. The second, that it exceed the noun by entering upon both it and the verb."},

    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: على الأصل.",
     "en": "That is, upon the root."},
]
